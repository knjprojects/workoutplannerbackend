import csv
from App.models import Book
from App.database import db
from flask import jsonify
def create_book( name, author, publisher,cover):
    newbook = Book(name=name, author=author, publisher=publisher,cover=cover)
    db.session.add(newbook)
    db.session.commit()
    return newbook

    """if row['height_m'] == '':
                row['height_m'] = None
            if row['weight_kg'] == '':
                row['weight_kg'] = None
            if row['type2'] == '':
                row['type2'] = None

def loadBooks():
    with open('books.csv', newline='', encoding='utf8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
           

            book = Book(name=row['name'], author=row['author'], publisher=row['publisher'],cover=row['cover'])
            db.session.add(book) 
        db.session.commit()
"""
def get_book_by_name(name):
    return Book.query.filter_by(name=name).first()

def get_book(id):
    return Book.query.get(id)

def get_all_books():
    return Book.query.all()

def get_all_books_json():
    books = Book.query.all()
    if not books:
        return []
    books = [book.get_json() for book in books]
    return books
def get_complete_books_data():
    data=[]
    books = Book.query.all()
    for book in books:
        total_rating = sum([review.rating for review in book.reviews])
        average_rating = total_rating / len(book.reviews)
        data.append({
            'id': book.id,
            'name': book.name,
            'author': book.author,
            'publisher': book.publisher,
            'cover':book.cover,
            'average_rating': average_rating,
            'reviews_count': len(book.reviews)
        })
    return jsonify(data)
         
"""def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None
    """
    