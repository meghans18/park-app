# first install plugins!!

# to run app first time (in python terminal):
# from app import db
# db.create_all()
# exit()

# python app.py (runs application on localhost:5000)

import os
import stripe
import requests
from requests.auth import HTTPBasicAuth
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from geopy.geocoders import Nominatim

stripe.api_key = "sk_test_51IaQy6CwKcZquRsXVvYz1eY7GlE7iSZqCVBXn9tnyBqjxQXQA6C3pVblvlKRJWpBn8gKgcpI6xbyUqxCAPO5iAZm00x4e83yRb"

# configuration
DEBUG = True

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "parkapp.db"))

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

#models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    privilege = db.Column(db.String(120), nullable=False) # 'regular', 'admin', 'towing'
    blocked = db.Column(db.Boolean, default=False)
    stripe_acct = db.Column(db.String(120), nullable=True)

    def __repr__(self):
        return '<User %r>' % self.email

class Spot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, nullable=False)
    addressNumber = db.Column(db.Integer, nullable=False)
    street = db.Column(db.String(80), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(20), nullable=False,)
    zipCode = db.Column(db.Integer, nullable=False)
    spotNumber = db.Column(db.Integer, nullable=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Spot %r>' % self.id


# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# helper methods
def find_lat_long(address):
    geolocator = Nominatim(user_agent="park-app")
    location = geolocator.geocode(address)
    return [location.latitude, location.longitude]

#routes
@app.route("/users", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            post_data = request.get_json()
            user = User(
                first_name=post_data.get('first_name'),
                last_name=post_data.get('last_name'),
                email=post_data.get('email'),
                password=post_data.get('password'),
                privilege='regular'
            )
            db.session.add(user)
            db.session.commit()
            return jsonify({
                'status': 'success',
                'privilege': 'regular',
                'message': 'Registration successful'
            })
        except Exception as e:
            return jsonify({
                'status': 'failed',
                'message': 'User already exists'
            })
    else:
        data = []
        users = User.query.all()
        for user in users:
            data.append({
                "id": user.id,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "privilege": user.privilege,
                "blocked": user.blocked,
            })
        return jsonify({
            'status': 'success',
            'users': data
        })

@app.route('/users/<user_id>', methods=['PUT', 'DELETE'])
def single_book(user_id):
    status = ''
    message = ''
    person = User.query.filter_by(id=user_id).first()
    if request.method == 'PUT':
        message = request.get_json().get('message')
        if message == 'blockUser':
            try:
                person.blocked = not person.blocked
                db.session.commit()
                status = 'success'
                message = 'User updated successfully'
            except Exception as e:
                return jsonify({
                    'status': 'failed',
                    'message': 'Update failed'
                })
        if message == 'changeTowing':
            try:
                if person.privilege == 'towing': person.privilege = 'regular'
                else: person.privilege = 'towing'
                db.session.commit()
                status = 'success'
                message = 'User updated successfully'
            except Exception as e:
                return jsonify({
                    'status': 'failed',
                    'message': 'Update failed'
                })
    if request.method == 'DELETE':
        try:
            db.session.delete(person)
            db.session.commit()
            status = 'success'
            message = 'User deleted successfully'
        except Exception as e:
            return jsonify({
                'status': 'failed',
                'message': 'Deletion failed'
            })
    return jsonify({
        'status': status,
        'message': message
    })

@app.route("/login", methods=['POST'])
def login():
    status = ''
    privilege = ''
    connected = 'no'
    message = ''
    try:
        post_data = request.get_json()
        email = post_data.get('email')
        password = post_data.get('password')
        loginPerson = User.query.filter_by(email=email).first()
        user_acct = loginPerson.stripe_acct
        if not user_acct is None: 
            stripe_info = stripe.Account.retrieve(user_acct)
            # stripe_info.details_submitted = False # use this line to test for accounts that haven't onboarded all the way
            if stripe_info.details_submitted:
                connected = 'yes'
            else:
                connected = 'partly'
        if loginPerson.blocked == True:
            return jsonify({
                'status': 'failed',
                'message': 'User is blocked',
            })
        if (loginPerson.password) == password:
            status = 'success'
            message = 'User Authenticated'
        else:
            status = 'failed'
            message = 'Cannot Authenticate'
        privilege = loginPerson.privilege
    except Exception as e:
            return jsonify({
                'status': 'failed',
                'message': "User doesn't exist"
            })
    return jsonify({
        'status': status,
        'privilege': privilege,
        'connected': connected,
        'message': message
    })

@app.route('/connect/<user_email>', methods=['GET'])
def connectUser(user_email):
    user = User.query.filter_by(email=user_email).first()
    if user.stripe_acct is None:
        account = stripe.Account.create(
            type="express",
            country="US",
            email=user.email,
        )
        user.stripe_acct = account.id
        db.session.commit()
    user = User.query.filter_by(email=user_email).first()
    account_links = stripe.AccountLink.create(
        account=user.stripe_acct,
        refresh_url='http://localhost:8080/refresh', #NEED TO DO
        return_url='http://localhost:8080/return',
        type='account_onboarding',
    )
    return jsonify({
        'status':'success',
        'url':account_links.url
    })

@app.route('/is-connected/<user_email>', methods=['GET'])
def checkConnected(user_email):
    user_acct = User.query.filter_by(email=user_email).first().stripe_acct
    stripe_req = stripe.Account.retrieve(user_acct)
    return jsonify({
        'status': 'success',
        'acct_info': stripe_req
    })

@app.route('/spots/<user_email>', methods=['GET'])
def userRegisteredSpots(user_email):
    data = []
    user_id = User.query.filter_by(email=user_email).first().id
    spots = Spot.query.filter_by(userId = user_id).all()
    for spot in spots:
        data.append({
            "id": spot.id,
            "userId": spot.userId,
            "addressNum": spot.addressNumber,
            "street": spot.street,
            "city": spot.city,
            "state": spot.state,
            "zipcode": spot.zipCode,
            "spotNumber": spot.spotNumber,
            "latitude": spot.latitude,
            "longitude": spot.longitude,
            "price": spot.price
        })
    return jsonify({
        'status': 'success',
        'spots': data
    })

@app.route("/spots", methods=['GET','POST'])
def spot():
    if request.method == 'POST':
        try:
            post_data = request.get_json()
            email = post_data.get('email')
            userId = User.query.filter_by(email=email).first().id
            address = "" + post_data.get('addressNum') + " " + post_data.get('street') + ", " + post_data.get('city') + ", " + post_data.get('state') + " " + post_data.get('zipcode')
            latLong = find_lat_long(address)
            spot = Spot(
            	userId = userId,
                addressNumber = post_data.get('addressNum'),
                street = post_data.get('street'),
                city = post_data.get('city'),
                state = post_data.get('state'),
                zipCode = post_data.get('zipcode'),
                spotNumber = post_data.get('spotNumber'),
                latitude = latLong[0],
                longitude = latLong[1],
                price = post_data.get('price')
            )
            db.session.add(spot)
            db.session.commit()
            return jsonify({
                'status': 'success',
                'message': 'Spot added!'
            })
        except Exception as e:
            return jsonify({
                'status': 'failed',
                'message': 'Failed to add spot'
            })
    else:
        data = []
        spots = Spot.query.all()
        for spot in spots:
            data.append({
                "id": spot.id,
                "userId": spot.userId,
                "addressNum": spot.addressNumber,
                "street": spot.street,
                "city": spot.city,
                "state": spot.state,
                "zipcode": spot.zipCode,
                "spotNumber": spot.spotNumber,
                "latitude": spot.latitude,
                "longitude": spot.longitude,
                "price": spot.price
            })
        return jsonify({
            'status': 'success',
            'spots': data
        })

@app.route('/spot/<spot_id>', methods=['GET'])
def specificSpot(spot_id):
    spot = Spot.query.filter_by(id = spot_id).first()
    data = {
        "id": spot.id,
        "userId": spot.userId,
        "addressNum": spot.addressNumber,
        "street": spot.street,
        "city": spot.city,
        "state": spot.state,
        "zipcode": spot.zipCode,
        "spotNumber": spot.spotNumber,
        "latitude": spot.latitude,
        "longitude": spot.longitude,
        "price": spot.price
    }
    return jsonify({
        'status': 'success',
        'spot': data
    })


@app.route("/")
def home():
    return "hello this is home page"

if __name__ == "__main__":
    app.run()