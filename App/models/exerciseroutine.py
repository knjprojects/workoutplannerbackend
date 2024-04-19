from App.database import db
class ExerciseRoutine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'), nullable=False)
    routine_id = db.Column(db.Integer, db.ForeignKey('routine.id'), nullable=False)

    def __init__(self, exercise_id, routine_id):
        self.exercise_id = exercise_id
        self.routine_id = routine_id

    def get_json(self):
        return {
            'id': self.id,
            'exercise_id': self.exercise_id,
            'routine_id': self.routine_id
        }
