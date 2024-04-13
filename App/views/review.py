from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user



from App.controllers import (

  get_all_reviews, 
  get_all_reviews_json,
  get_review,
  get_user_reviews,
  get_book_reviews,get_user
)

review_views = Blueprint('review_views', __name__, template_folder='../templates')

@review_views.route('/reviews', methods=['GET'])
def get_reviews_page():
    reviews = get_all_reviews_json()
    return render_template('reviews.html', reviews=reviews)

@review_views.route('/reviews/<int:bookid>', methods=['GET'])
def get_reviews_book(bookid):
    reviews = get_all_reviews_json()
    books = get_book_reviews(bookid)
    return render_template('books.html',books=books, reviews=reviews)

@review_views.route('/reviews', methods=['POST'])
@jwt_required()
def create_review_action():
    data = request.form
    flash(f"Review created!")
    usa=get_user(jwt_current_user.id)
    usa.review_book(data['bookid'], data['rating'], data['reviewtext'])
    return redirect(url_for('review_views.get_reviews_page'))

@review_views.route('/api/reviews', methods=['GET'])
def get_reviews_action():
    reviews = get_all_reviews_json()
    return jsonify(reviews)

""""@review_views.route('/api/reviews', methods=['POST'])
def create_review_endpoint():
    data = request.json
    book = create_book(data['bookname'], data['author'], data['publisher'],data['cover])
    return jsonify({'message': f"book {book.name} created with id {book.id}"})
"""
@review_views.route('/static/reviews', methods=['GET'])
def static_review_page():
  return send_from_directory('static', 'static-review.html')