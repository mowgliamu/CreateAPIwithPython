"""Create API with Python.

@Author: Prateek Goel
@Date: 2020-12-07
@Email: prateik.goel@gmail.com
@Last modified by: Prateek Goel
@Last modified time: 2020-12-07

"""

import os
import json
from flask import Flask, Blueprint, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, validate
from marshmallow.exceptions import ValidationError

# Create a new Flask application
app = Flask(__name__)

# Create API Blueprint instance
api = Blueprint('api', __name__)

# Warning suppresion
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Set up SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///catalogue.db'
db = SQLAlchemy(app)

port = int(os.environ.get('PORT', 8080))


class Book(db.Model):
    """Book database object using SQLAlchemy."""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    author = db.Column(db.String(50))
    publisher = db.Column(db.String(50))
    published_year = db.Column(db.Integer)

    @classmethod
    def from_dict(cls, data):
        return Book(title=data['title'], author=data['author'],
         publisher=data['publisher'], published_year=data['published_year'])

    def __repr__(self):
        return f'<Book: { self.title }>'


# Create Database
db.create_all()


class BookSchema(Schema):
    """Schema abstraction layer for Book model using Marshmallow."""

    id = fields.Int()
    title = fields.Str(required=True, validate=validate.Length(
        min=1, error="Field should not be empty."))
    author = fields.Str(required=True, validate=validate.Length(
        min=1, error="Field should not be empty."))
    publisher = fields.Str(required=True, validate=validate.Length(
        min=1, error="Field should not be empty."))
    published_year = fields.Int(required=True, validate=validate.Range(
        min=1, max=2020, error="Futuristic books are not yet allowed."))


@api.errorhandler(400)
def bad_request(e):
    return {'error': e.description, 'status code': 400}, 400


@api.errorhandler(404)
def bad_request(e):
    return {'error': 'Not Found'}, 404


@api.errorhandler(500)
def bad_request(e):
    return {'error': 'Internal Server Error'}, 500


@api.route('/books', methods=['GET'])
def get_books():
    """GET request to retrieve all books in the database."""
    books = Book.query.order_by(Book.title).all()
    all_books = []
    for book in books:
        new_book = {
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "publisher": book.publisher,
            "published_year": book.published_year
        }

        all_books.append(new_book)
    return json.dumps(all_books), 200


@api.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    """GET request to retrieve a book by id."""
    book = Book.query.get_or_404(book_id)

    return book_schema.dump(book)


@api.route('/books', methods=['POST'])
def create_books():
    """POST request to create books from a database."""
    json_data = request.get_json()
    success_books = []
    failed_result = {}
    for index, obj in enumerate(json_data):
        try:
            book = book_schema.load(obj)
            success_books.append(book)
        except ValidationError as err:
            failed_result[index] = {'error': err.messages, 'status code': 400}

    # Add successful books to the database
    db.session.bulk_insert_mappings(Book, success_books)
    db.session.commit()

    return failed_result


@api.route('/books/<int:book_id>', methods=['PUT'])
def edit_book(book_id):
    """PUT request to edit a book by id."""
    json_data = request.get_json()

    try:
        book_data = book_schema.load(json_data, partial=True)
    except ValidationError as err:
        abort(400, err.messages)

    book_query = Book.query.filter_by(id=book_id)
    update_count = book_query.update(book_data)

    if update_count == 0:
        abort(404)
    else:
        pass

    db.session.commit()

    book = book_query.first()
    return book_schema.dump(book)


@api.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    """DELETE request to delete a book by id."""
    del_count = Book.query.filter_by(id=book_id).delete()

    if del_count == 0:
        abort(404)
    else:
        pass

    db.session.commit()

    return {}, 204


if __name__ == '__main__':
    book_schema = BookSchema()
    app.register_blueprint(api)
    app.run(host="0.0.0.0", port=port)


