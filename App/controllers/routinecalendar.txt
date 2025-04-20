from App.database import db
from App.models import RoutineCalendar

"""def createRoutineCalendarEntry(date, routine_id, calendar_integration_id):
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
        
"""
def createRoutineCalendarEntry(date, user_id, routine_id, calendar_integration_id,time):
    routine_calendar = RoutineCalendar(date=date, user_id=user_id, routine_id=routine_id, calendar_integration_id=calendar_integration_id,time=time)
    try:
                
                db.session.add(routine_calendar)
                db.session.commit()
                
                return  routine_calendar.get_json() 
    except Exception as e:
                print(e)
                db.session.rollback()
                return None
   #create time specific get for routineentry, right now we fetch day alone, change this query to .all()
def getRoutineCalendarEntryForUser(user_id, date, calendar_id):
        routinecals=RoutineCalendar.query.filter_by(user_id=user_id,date=date,calendar_integration_id=calendar_id).all()
        if not routinecals:
                return None
        routines_list=[routine.get_json for routine in routinecals]
        return routines_list
        return routine.get_json()
        

def getRoutineCalendarByTime(user_id,date,calendar_id,time):
        rc=RoutineCalendar.query.filter_by(user_id=user_id,date=date,calendar_integration_id=calendar_id,time=time).first()
        if not rc:
                return None
        return rc.get_json()

def getAllRoutineCalendars():
        try:
                routinecals = RoutineCalendar.query.all()
                if not routinecals:
                        return []
                routinecals_list = [calendar.get_json() for calendar in routinecals]
                return routinecals_list
        except Exception as e:
        #logging.error(f"Error occurred in list_cals: {e}")
                return []
    
