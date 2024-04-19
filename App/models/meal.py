from App.database import db
class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    food_item_id = db.Column(db.Integer, db.ForeignKey('food_item.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, food_item_id, user_id):
        self.food_item_id = food_item_id
        self.user_id = user_id

    def get_json(self):
        return {
            'id': self.id,
            'food_item_id': self.food_item_id,
            'user_id': self.user_id
        }