import csv
from flask import jsonify
from App.models import FoodItem
from App.database import db

def loadFoods():
    with open('food.csv', newline='', encoding='utf8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:#ingredients,protein,carbs,fat,calories,dietrestrict,image
            food = FoodItem(name=row['name'],description=row['description'],ingredients=row['ingredients'],protein=row['protein'],carbs=row['carbs'],fat=row['fat'],calories=row['calories'], dietrestrict=row['dietrestrict'],image=row['image'])
            db.session.add(food)
    db.session.commit()

def list_foods():
    foods=FoodItem.query.all()
    if not foods:
        return []
    foods_list = [food.get_json() for food in foods]
    return foods_list

def getFoodById(foodid):
    food=FoodItem.query.filter_by(id=foodid).first()
    if not food:
        return None
    return food.get_json()


    