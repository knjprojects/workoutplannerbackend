from App.database import db
class RoutineCalendar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    routine_id = db.Column(db.Integer, db.ForeignKey('routine.id'))
    calendar_integration_id = db.Column(db.Integer, db.ForeignKey('calendar_integration.id'))

    def __init__(self, routine_id, calendar_integration_id):
        self.routine_id = routine_id
        self.calendar_integration_id = calendar_integration_id

    def get_json(self):
        return {
            'id': self.id,
            'routine_id': self.routine_id,
            'calendar_integration_id': self.calendar_integration_id
        }