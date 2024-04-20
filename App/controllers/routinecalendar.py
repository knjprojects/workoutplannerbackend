from App.database import db
from App.models import RoutineCalendar

def createRoutineCalendarEntry(date, routine_id, calendar_integration_id):
    routine_calendar = RoutineCalendar(date=date, routine_id=routine_id, calendar_integration_id=calendar_integration_id)
    try:
                
                db.session.add(routine_calendar)
                db.session.commit()
               
                return routine_calendar
    except Exception as e:
                print(e)
                db.session.rollback()
                return None
   
def getRoutineCalendarEntryForUser(user_id, date, calendar_id):
        routines=RoutineCalendar.query.filter_by(user_id=user_id,date=date,calendar_integration_id=calendar_id).all()
        if not routines:
                return []
        routines_list=[routine.get_json for routine in routines]
        return routines_list
        

    
