from flask import jsonify
from App.database import db
from App.models import MealCalendar

def createMealCalendarEntry(date, user_id, meal_id, calendar_integration_id):
    meal_calendar = MealCalendar(date=date, user_id=user_id, meal_id=meal_id, calendar_integration_id=calendar_integration_id)
    try:
                
                db.session.add(meal_calendar)
                db.session.commit()
                #mcel=MealCalendar.query.filter_by(user_id=user_id,date=date).first()
                return  meal_calendar.get_json() #meal_calendar
    except Exception as e:
                print(e)
                db.session.rollback()
                return None
   
def getMealCalendarEntryForUser(user_id, date, calendar_id):
        meals=MealCalendar.query.filter_by(user_id=user_id,date=date,calendar_integration_id=calendar_id).all()
        if not meals:
                return []
        meals_list=[meal.get_json for meal in meals]
        return jsonify(meals_list)
        
