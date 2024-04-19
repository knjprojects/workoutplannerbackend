from App.database import db
from App.models import Routine, Exercise, User, ExerciseRoutine

"""def test_routine_exercise_relationship():
    user = User.query.get(1)
    routine = Routine(name='Test Routine', description='Test Routine', user_id=user.id)
    exercise1 = Exercise.query.get(1)
    exercise2 = Exercise.query.get(2)
    routine.exercises.append(exercise1)
    routine.exercises.append(exercise2)
    db.session.add(routine)
    db.session.commit()
    loaded_routine = Routine.query.get(routine.id)
    assert len(loaded_routine.exercises) == 2
    assert loaded_routine.exercises[0].id == exercise1.id
    assert loaded_routine.exercises[1].id == exercise2.id"""


def addExerciseToRoutine(routine_id,exercise_id):
        try:
                routineexercise=ExerciseRoutine(routine_id=routine_id, exercise_id=exercise_id)
                db.session.add(routineexercise)
                db.session.commit()
                return routineexercise
        except Exception as e:
                print(e)
                db.session.rollback()
                return None
        
#all exercises in all routines
def list_routine_exercises():
        rxs=ExerciseRoutine.query.all()
        if not rxs:
                return []
       
        rx_list = [rx.get_json() for rx in rxs]
        return rx_list
        

#all exercises for a specific routine
def list_routine_exercise_by_routine(routine_id):
        rxs=ExerciseRoutine.query.filter_by(routine_id=routine_id)
        if not rxs:
                return None
        rxs_list=[rx.get_json() for rx in rxs]
        