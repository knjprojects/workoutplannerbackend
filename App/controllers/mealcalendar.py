from flask import jsonify
from App.database import db
from App.models import MealCalendar

def createMealCalendarEntry(date, user_id, meal_id, calendar_integration_id,time):
    meal_calendar = MealCalendar(date=date, user_id=user_id, meal_id=meal_id, calendar_integration_id=calendar_integration_id,time=time)
    try:
                
                db.session.add(meal_calendar)
                db.session.commit()
                
                return  meal_calendar.get_json() 
    except Exception as e:
                print(e)
                db.session.rollback()
                return None
#add time specific, because we are fetching by date here, change the be;low query to .all|()
def getMealCalendarEntryForUser(user_id, date, calendar_id):
        meal=MealCalendar.query.filter_by(user_id=user_id,date=date,calendar_integration_id=calendar_id).first()
        if not meal:
                return None
        #meals_list=[meal.get_json for meal in meals]
        #return jsonify(meal)
        return meal.get_json()


def getMealCalendarByTime(user_id,date,calendar_id,time):
        meal=MealCalendar.query.filter_by(user_id=user_id,date=date,calendar_integration_id=calendar_id,time=time).first()
        if not meal:
                return None
        return meal.get_json()

def getAllMealCalendars():
        try:
                mealcals = MealCalendar.query.all()
                if not mealcals:
                        return []
                mealcals_list = [calendar.get_json() for calendar in mealcals]
                return mealcals_list
        except Exception as e:
        #logging.error(f"Error occurred in list_cals: {e}")
                return []