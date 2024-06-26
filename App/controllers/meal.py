from App.database import db
from App.models import Meal
def createMeal(user_id,food_id):
    meal=Meal(user_id=user_id,food_item_id=food_id)
    try:
                
                
                db.session.add(meal)
                db.session.commit()
                return meal.get_json()
    except Exception as e:
                print(e)
                db.session.rollback()
                return None
    
def getMeals():
    meals=Meal.query.all()
    if not meals:
            return []
    meal_list=[]
    meal_list = [meal.get_json() for meal in meals]
    return meal_list
    
def mealsForUser(user_id):
        meals=Meal.query.filter_by(user_id=user_id).all()
        if not meals:
                return []
        meal_list=[]
        meal_list=[meal.get_json() for meal in meals]
        return meal_list

def removeMeal(meal_id):
        meal=Meal.query.filter_by(meal_id=meal_id).first()
        try: 
                db.session.remove(meal)
                db.session.commit()
        except Exception as e:
                print(e)
                db.session.rollback()
                return None

