from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    review = db.relationship('Review', backref='user',lazy=True)


    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def get_json(self):
        return{
            'id': self.id,
            'username': self.username
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def update_user(self, username):
        self.username = username
        db.session.add(self)
        db.session.commit()
        return self
        return None
    # to svoifd circular import issue on render, im importing it using a lazy import instead top of the file
    def review_book(self, book_id, rating, reviewtext):
        from App.models import Book
        from App.controllers import create_review
        book = Book.query.get(book_id)
        if book:
            try:
                
                review = create_review(self.id, book_id, rating, reviewtext)
                return review
            except Exception as e:
                print(e)
                db.session.rollback()
                return None
        return None

    def delete_review(self, review_id):
        from App.models import Review
        review = Review.query.get(review_id)
        if review.user == self:
            db.session.delete(review)
            db.session.commit()
            return True
        return None

    def update_review(self, review_id, reviewtext, rating):
        from App.models import Review
        review = Review.query.get(review_id)
        if review.user == self:
            review.reviewtext = reviewtext
            review.rating = rating
            db.session.add(review)
            db.session.commit()
            return True
        return None