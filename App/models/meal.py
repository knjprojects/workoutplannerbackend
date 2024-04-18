from App.database import db

class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(255))
    food_items = db.relationship('MealFoodItem', backref='meal', lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, name, description, user_id):
        self.name = name
        self.description = description
        self.user_id = user_id

    def get_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'user_id': self.user_id,
            'food_items': [food_item.get_json() for food_item in self.food_items]
        }