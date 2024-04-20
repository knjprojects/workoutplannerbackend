from App.database import db
class CalendarIntegration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(200))
    #routines = db.relationship('RoutineCalendar', backref='calendar_integration', lazy=True)
    #meals = db.relationship('MealCalendar', backref='calendar_integration', lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    timezone=db.Column(db.String(100), nullable=False)
    def __init__(self, date, user_id, timezone):
        self.date = date
        self.user_id = user_id
        self.timezone=timezone

    def get_json(self):
        return {
            'id': self.id,
            'date': self.date,
            'user_id': self.user_id,
            'timezone':self.timezone
            #'routines': [routine_calendar.get_json() for routine_calendar in self.routines],
            #'meals': [meal_calendar.get_json() for meal_calendar in self.meals]
        }

    

    