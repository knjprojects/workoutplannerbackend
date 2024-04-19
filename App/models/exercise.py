from App.database import db
class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    description = db.Column(db.String(255),nullable=False)
    muscle = db.Column(db.String(50),nullable=False)
    equipment = db.Column(db.String(100),nullable=False)
    difficulty = db.Column(db.String(50),nullable=False)
    image = db.Column(db.String(200),nullable=False)
    routines = db.relationship('ExerciseRoutine', backref='exercise', lazy=True)

    def __init__(self, name, description, muscle, equipment, difficulty, image):
        self.name = name
        self.description = description
        self.muscle = muscle
        self.equipment = equipment
        self.difficulty = difficulty
        self.image = image

    def get_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'muscle': self.muscle,
            'equipment': self.equipment,
            'difficulty': self.difficulty,
            'image': self.image,
            'routines': [routine_exercise.get_json() for routine_exercise in self.routines]
        }