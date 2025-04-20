from App.models import Routine
from App.database import db

def createRoutine(user_id,routinename,description, prefs, fgoals):
    try:
                
                routine=Routine(user_id=user_id,name=routinename,description=description,prefs=prefs,fgoals=fgoals)
                db.session.add(routine)
                db.session.commit()
                return routine
    except Exception as e:
                print(e)
                db.session.rollback()
                return None
    
def list_routines():
    routines=Routine.query.all()
    if not routines:
        return []
    routines_list = [routine.get_json() for routine in routines]
    return routines_list

def get_user_routines(user_id):
       routines=Routine.query.filter_by(user_id=user_id).all()
       if not routines:
        return []
       routines_list = [routine.get_json() for routine in routines]
       return routines_list



