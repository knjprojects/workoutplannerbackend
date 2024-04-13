from App.database import db
class Review(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
  review = db.relationship('Book')
  reviewtext = db.Column(db.String(255))
  rating=db.Column((db.Integer), nullable=False)
  
  def __init__(self, user_id, book_id, rating, reviewtext):
    self.user_id = user_id
    self.book_id = book_id
    self.rating = rating
    self.reviewtext = reviewtext
  
  def __repr__(self):
      return f'<Review {self.id} : {self.reviewtext} book {self.book.name}>'
  

  def setReviewText(self,reviewtext):
     self.reviewtext=reviewtext
    
  def setRating(self,rating):
     self.rating=rating
  
  def get_json(self):
    return{
      'id': self.id,
      'user_id': self.user.id,
      'book_name': self.book.name,
      'user_name':self.user.username,
      #'book_id': self.book.id,
      'rating': self.rating,
      'reviewtext': self.reviewtext
    }
    
 