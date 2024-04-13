from App.database import db
class Book(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)
  author = db.Column(db.String(255),nullable=False)
  cover = db.Column(db.String(255),nullable=False)
  publisher = db.Column(db.String(255),nullable=False)
  reviews_count = db.Column(db.Integer, default=0)
  reviews = db.relationship('Review', backref='book', lazy=True)
  def __init__(self, name, author, publisher, cover):
    self.name = name
    self.author = author
    self.publisher = publisher
    self.cover = cover
    self.reviews_count=0
    
  def __repr__(self):
      return f'<Book {self.id} : {self.name} author {self.author} publisher {self.publisher}>'
    
  def get_json(self):
    return {
      'id': self.id,
      'name': self.name,
      'author': self.author,
      'publisher': self.publisher,
      'cover' : self.cover,
      'reviews_count': self.reviews_count,
  }