# first install plugins!!

# to run app first time (in python terminal):
# from app import db
# db.create_all()
# exit()

# python app.py (runs application on localhost:5000)

import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

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

BOOKS = [
	{
		'title': 'On the Road',
		'author': 'Jack Kerouac',
		'read': True
	}
]

#models
class Book(db.Model):
    title = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)

    def __repr__(self):
        return "<Title: {}>".format(self.title)

class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(400), nullable=False)
    priority = db.Column(db.String(10), nullable=False, default="user")

    def __repr__(self):
        return '<User %r>' % self.email

class spot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address_number = db.Column(db.Integer, nullable=False)
    street = db.Column(db.String(80), nullable=False)
    city = db.Column(db.String(50), unique=True, nullable=False)
    state = db.Column(db.String(20), nullable=False, default="user")
    zip_code = db.Column(db.Integer, nullable=False)
    spot_number = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return '<Spot %r>' % self.id
		
# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route("/books", methods=["GET"])
def return_books():
	return jsonify({
		'status': 'success',
		'books': BOOKS
	})

@app.route("/register", methods=['POST'])
def register():
	response_object = {'status': 'success'}
	if request.method == 'POST':
		post_data = request.get_json()
		user.append({
			'first_name': post_data.get('first_name'),
		    'last_name': post_data.get('last_name'),
			'email': post_data.get('email'),
			'password': post_data.get('password')
		})
		response_object['message'] = 'User Registered!'

@app.route("/spot", methods=['POST'])
def spot():
	response_object = {'status': 'success'}
	if request.method == 'POST':
		post_data = request.get_json()
		user.append({
			'address_number': post_data.get('address_number'),
		    'street': post_data.get('street'),
			'city': post_data.get('city'),
			'state': post_data.get('state'),
			'zip_code': post_data.get('zip_code'),
			'spot_number': post_data.get('spot_number')
		})
		response_object['message'] = 'Spot Registered!'


@app.route("/")
def home():
	return "hello this is home page"

@app.route("/ping", methods=["GET", "POST"])
def practice():
	status = 'success'
	if request.method == 'POST':
		try:
			post_data = request.get_json();
			book = Book(title = post_data.get("title"))
			db.session.add(book)
			db.session.commit()
		except Exception as e:
			return jsonify({
				'status': 'failed',
				'message': 'duplicate book title'
			})
	data = []
	books = Book.query.all()
	for book in books:
		data.append({
			"title": book.title,
		})
	return jsonify({
		'status': status,
		'books': books
	})
  
if __name__ == "__main__":
    app.run()