from App.database import db
class Routine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    description = db.Column(db.String(255),nullable=False)
    exercises = db.relationship('ExerciseRoutine', backref='routine', lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    prefs = db.Column(db.String(50))  # Example: Vegetarian, Vegan, Gluten-free
    fgoals = db.Column(db.String(50))  # Example: Weight loss, Muscle gain, Maintenance

    def __init__(self, name, description, user_id,prefs,fgoals):
        self.name = name
        self.description = description
        self.user_id = user_id
        self.prefs=prefs
        self.fgoals=fgoals

    def get_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'user_id': self.user_id,
            'prefs':self.prefs,
            'fgoals':self.fgoals,
            'exercises': [exercise_routine.get_json() for exercise_routine in self.exercises]
        }

    