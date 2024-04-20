from App.database import db
from App.models import CalendarIntegration

def createCalendar(date,user_id,timezone):
    calendar=CalendarIntegration(user_id=user_id,date=date,timezone=timezone)
    try:
                
                
                db.session.add(calendar)
                db.session.commit()
                return calendar
    except Exception as e:
                print(e)
                db.session.rollback()
                return None


def list_cals():
        calendars=CalendarIntegration.query.all()
        if not calendars:
            return []
        calendars_list=[calendar.get_json for calendar in calendars]
        return calendars_list
            
def get_user_calendars(userid):
        calendars=CalendarIntegration.query.filter_by(user_id=userid).all()
        if not calendars:
                return []
        calendars_list=[calendar.get_json for calendar in calendars]
        return calendars_list