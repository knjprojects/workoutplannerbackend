from App.database import db
class MealCalendar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(200),nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    calendar_integration_id = db.Column(db.Integer, db.ForeignKey('calendar_integration.id'), nullable=False)
    meal_id = db.Column(db.Integer, db.ForeignKey('meal.id'), nullable=False)

    meal = db.relationship('Meal', backref='meal_calendars', lazy=True)
    #calendar_integration = db.relationship('CalendarIntegration', backref='meal_calendars', lazy=True)
    integration = db.relationship('CalendarIntegration', backref='meal_calendars', lazy=True)
    def __init__(self, date, user_id, meal_id, calendar_integration_id):
        self.date = date
        self.user_id = user_id
        self.meal_id = meal_id
        self.calendar_integration_id = calendar_integration_id

    def get_json(self):
        return {
            'id': self.id,
            'date': self.date,
            'user_id': self.user_id,
            'meal_id': self.meal_id,
            'calendar_integration_id': self.calendar_integration_id,
            'meal': self.meal.get_json()
        }