from App.database import db
class RoutineCalendar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(100),nullable=False)
    routine_id = db.Column(db.Integer, db.ForeignKey('routine.id'))
    calendar_integration_id = db.Column(db.Integer, db.ForeignKey('calendar_integration.id'))
    routine = db.relationship('Routine', backref='routine_calendars', lazy=True)
    def __init__(self, date, routine_id, calendar_integration_id):
        self.date = date
        self.routine_id = routine_id
        self.calendar_integration_id = calendar_integration_id

    def get_json(self):
        return {
            'id': self.id,
            'date': self.date,
            'routine_id': self.routine_id,
            'calendar_integration_id': self.calendar_integration_id,
            'routine': self.routine.get_json()
        }


