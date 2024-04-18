from App.database import db
from App.models import Routine, Exercise, User

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