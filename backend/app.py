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
		
# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route("/books", methods=["GET"])
def return_books():
	return jsonify({
		'status': 'success',
		'books': BOOKS
	})

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