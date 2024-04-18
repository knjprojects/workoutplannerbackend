from App.database import db
class MealFoodItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meal_id = db.Column(db.Integer, db.ForeignKey('meal.id'))
    food_item_id = db.Column(db.Integer, db.ForeignKey('food_item.id'))
    quantity = db.Column(db.Integer, nullable=False)

    def __init__(self, meal_id, food_item_id, quantity):
        self.meal_id = meal_id
        self.food_item_id = food_item_id
        self.quantity = quantity

    def get_json(self):
        return {
            'id': self.id,
            'meal_id': self.meal_id,
            'food_item_id': self.food_item_id,
            'quantity': self.quantity
        }