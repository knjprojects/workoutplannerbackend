from App.database import db
from App.models import Meal
def createMeal(user_id,food_id):
    meal=Meal(user_id=user_id,food_item_id=food_id)
    try:
                
                
                db.session.add(meal)
                db.session.commit()
                return meal
    except Exception as e:
                print(e)
                db.session.rollback()
                return None
    
def loadMeals():
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


