from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user



from App.controllers import (
    get_all_books,
    create_book,
    get_all_books_json,get_complete_books_data

)

book_views = Blueprint('book_views', __name__, template_folder='../templates')

@book_views.route('/books', methods=['GET'])
def get_book_page():
    books = get_all_books()#get_complete_books_data()#
    return render_template('books.html', books=books)

@book_views.route('/books', methods=['POST'])
def create_book_action():
    data = request.form
    flash(f"Book {data['bookname']} created!")
    create_book(data['bookname'], data['author'], data['publisher'],data['cover'])
    return redirect(url_for('book_views.get_book_page'))

@book_views.route('/api/books', methods=['GET'])
def get_books_action():
    books = get_all_books_json()
    return jsonify(books)

@book_views.route('/api/books', methods=['POST'])
def create_book_endpoint():
    data = request.json
    book = create_book(data['bookname'], data['author'], data['publisher'],data['cover'])
    return jsonify({'message': f"book {book.name} created with id {book.id}"})

@book_views.route('/static/books', methods=['GET'])
def static_book_page():
  return send_from_directory('static', 'static-book.html')