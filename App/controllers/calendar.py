from App.database import db
from App.models import CalendarIntegration

def createCalendar(date,user_id,timezone):
    calendar=CalendarIntegration(user_id=user_id,date=date,timezone=timezone)
    try:
        db.session.add(calendar)
        db.session.commit()
        #cal=CalendarIntegration.query.filter_by(user_id=user_id).first()
        return calendar
    except Exception as e:
        print(e)
        db.session.rollback()
        return None


def list_cals():
    try:
        calendars = CalendarIntegration.query.all()
        if not calendars:
            return []
        calendars_list = [calendar.get_json() for calendar in calendars]
        return calendars_list
    except Exception as e:
        #logging.error(f"Error occurred in list_cals: {e}")
        return []
            
def get_user_calendars(user_id):# changed all to first
    try:
        calendars = CalendarIntegration.query.filter_by(id=1).first()
        if not calendars:
            return []
        #calendars_list = [calendar.get_json() for calendar in calendars]
        return calendars
    except Exception as e:
        #logging.error(f"Error occurred in get_user_calendars for user_id {user_id}: {e}")
        return []