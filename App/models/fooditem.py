from flask import jsonify
from App.database import db
class FoodItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(255), nullable=False)
    ingredients = db.Column(db.String(255),nullable=False)
    protein = db.Column(db.Integer,nullable=False)
    carbs = db.Column(db.Integer, nullable=False)
    fat = db.Column(db.Integer, nullable=False)
    calories = db.Column(db.Integer, nullable=False)
    dietrestrict = db.Column(db.String(100),nullable=False)#vegetarian, "vegan "gluten free
    image=db.Column(db.String(255),nullable=False)

    def __init__(self, name, description, ingredients, protein, carbs, fat, calories, dietrestrict, image):
        self.name = name
        self.description = description
        self.ingredients = ingredients
        self.protein = protein
        self.carbs = carbs
        self.fat = fat
        self.calories = calories
        self.dietrestrict = dietrestrict
        self.image = image

    def get_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'ingredients': self.ingredients,
            'protein': self.protein,
            'carbs': self.carbs,
            'fat': self.fat,
            'calories': self.calories,
            'dietrestrict':self.dietrestrict,
            'image': self.image
        }

