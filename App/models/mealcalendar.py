from App.database import db
class MealCalendar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meal_id = db.Column(db.Integer, db.ForeignKey('meal.id'))
    calendar_integration_id = db.Column(db.Integer, db.ForeignKey('calendar_integration.id'))

    def __init__(self, meal_id, calendar_integration_id):
        self.meal_id = meal_id
        self.calendar_integration_id = calendar_integration_id

    def get_json(self):
        return {
            'id': self.id,
            'meal_id': self.meal_id,
            'calendar_integration_id': self.calendar_integration_id
        }