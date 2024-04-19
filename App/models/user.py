from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False, unique=True)
    email =  db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    gender = db.Column(db.String(120), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    weight= db.Column(db.Integer, nullable=False)
    review = db.relationship('Review', backref='user',lazy=True)
    image=db.Column(db.String(25))

    budget=db.Column(db.Integer, nullable=False)

    
    routines = db.relationship('Routine', backref='user', lazy=True)
    
    meals = db.relationship('Meal', backref='user', lazy=True)
    calendar_integrations = db.relationship('CalendarIntegration', backref='user', lazy=True)

    def __init__(self, username,email, password, budget,gender, age, weight):
        self.username = username
        self.email=email
        
        self.budget=budget
        self.gender=gender
        self.age=age
        self.weight=weight
        self.image=""
        self.set_password(password)

    def get_json(self):
        return{
            'id': self.id,
            'username': self.username,
            'email':self.email,
            'budget':self.budget,
            'gender':self.gender,
            'weight':self.weight,
            'age':self.age,
            'image':self.image,
            'routines': self.routines,
            'meals':self.meals,
            'calendar':self.calendar_integrations
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def update_user_basic(self, username,email,image):
        self.username = username
        self.image=image
        self.email=email
        
        db.session.add(self)
        db.session.commit()
        return self
    def update_user_sensitive(self,budget,weight,prefs,fgoals, age):
        self.budget=budget
        self.weight=weight
        self.prefs=prefs
        self.fgoals=fgoals
        self.age=age
        db.session.add(self)
        db.session.commit()
        return self
        
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