from App.database import db
class CalendarIntegration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(200))
    routines = db.relationship('RoutineCalendar', backref='calendar_integration', lazy=True)
    #meals = db.relationship('MealCalendar', backref='calendar_integration', lazy=True)
    meals = db.relationship('MealCalendar', backref='calendar_integration', lazy=True)
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
            'timezone':self.timezone,
            'routines': [routine_calendar.get_json() for routine_calendar in self.routines],
            'meals': [meal_calendar.get_json() for meal_calendar in self.meals]
        }

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

class FoodItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(255), nullable=False)
    ingredients = db.Column(db.String(255),nullable=False)
    protein = db.Column(db.Integer,nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    carbs = db.Column(db.Integer, nullable=False)
    fat = db.Column(db.Integer, nullable=False)
    calories = db.Column(db.Integer, nullable=False)
    dietrestrict = db.Column(db.String(100),nullable=False)#vegetarian, "vegan "gluten free
    image=db.Column(db.String(255),nullable=False)
    meal = db.relationship('Meal', backref='food_item', lazy=True)

    def __init__(self, name, description, ingredients, protein, carbs, fat, calories, dietrestrict, image,cost):
        self.name = name
        self.description = description
        self.ingredients = ingredients
        self.protein = protein
        self.carbs = carbs
        self.fat = fat
        self.calories = calories
        self.dietrestrict = dietrestrict
        self.image = image
        self.cost=cost

    def get_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'ingredients': self.ingredients,
            'protein': self.protein,
            'carbs': self.carbs,
            'fat': self.fat,
            'calories': self.calories,
            'dietrestrict':self.dietrestrict,
            'cost':self.cost,
            'image': self.image
            #'meals': [meal.get_json() for meal in self.meals]
        }
class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    food_item_id = db.Column(db.Integer, db.ForeignKey('food_item.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    
   
    #backref could also be noneuser = db.relationship('User', backref='meals', lazy=True)

    def __init__(self, food_item_id, user_id):
        self.food_item_id = food_item_id
        self.user_id = user_id

    def get_json(self):
        return {
            'id': self.id,
            'food_item_id': self.food_item_id,
            'user_id': self.user_id,
            'food_item': self.food_item.get_json(),
            'user': self.user.get_json()
        }
    
    from App.database import db
class MealCalendar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(200),nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    calendar_integration_id = db.Column(db.Integer, db.ForeignKey('calendar_integration.id'), nullable=False)
    meal_id = db.Column(db.Integer, db.ForeignKey('meal.id'), nullable=False)
    time=db.Column(db.String(200), nullable=False)
    meal = db.relationship('Meal', backref='meal_calendars', lazy=True)
    #calendar_integration = db.relationship('CalendarIntegration', backref='meal_calendars', lazy=True)
    integration = db.relationship('CalendarIntegration', backref='meal_calendars', lazy=True)
    def __init__(self, date, user_id, meal_id, calendar_integration_id,time):
        self.date = date
        self.user_id = user_id
        self.meal_id = meal_id
        self.calendar_integration_id = calendar_integration_id
        self.time=time

    def get_json(self):
        return {
            'id': self.id,
            'date': self.date,
            'user_id': self.user_id,
            'meal_id': self.meal_id,
            'time':self.time,
            'calendar_integration_id': self.calendar_integration_id,
            'meal': self.meal.get_json()
        }
    
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

class RoutineCalendar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(100),nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    time=db.Column(db.String(200), nullable=False)
    routine_id = db.Column(db.Integer, db.ForeignKey('routine.id'))
    calendar_integration_id = db.Column(db.Integer, db.ForeignKey('calendar_integration.id'))
    routine = db.relationship('Routine', backref='routine_calendars', lazy=True)
    def __init__(self, date, routine_id, calendar_integration_id,user_id,time):
        self.date = date
        self.user_id=user_id
        self.routine_id = routine_id
        self.calendar_integration_id = calendar_integration_id
        self.time=time

    def get_json(self):
        return {
            'id': self.id,
            'date': self.date,
            'time':self.time,
            'routine_id': self.routine_id,
            'calendar_integration_id': self.calendar_integration_id,
            'user_id':self.user_id,
            'routine': self.routine.get_json()
        }
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False, unique=True)
    email =  db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    gender = db.Column(db.String(120), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    weight= db.Column(db.Integer, nullable=False)
    height= db.Column(db.String(100), nullable=False)

    #review = db.relationship('Review', backref='user',lazy=True)

    image=db.Column(db.String(25))

    budget=db.Column(db.Integer, nullable=False)

    
    routines = db.relationship('Routine', backref='user', lazy=True)
    meals = db.relationship('Meal', backref='user', lazy=True)
    meal_calendars = db.relationship('MealCalendar', backref='user', lazy=True)
    calendar_integrations = db.relationship('CalendarIntegration', backref='user', lazy=True)
    def __init__(self, username,email, password, budget,gender, age, weight,height):
        self.username = username
        self.email=email
        self.budget=budget
        self.gender=gender
        self.age=age
        self.weight=weight
        self.image=""
        self.height=height
        self.set_password(password)

    def get_json(self):
        return{
            'id': self.id,
            'username': self.username,
            'email':self.email,
            'budget':self.budget,
            'gender':self.gender,
            'weight':self.weight,
            'height':self.height,
            'age':self.age,
            'image':self.image
            #'meals': [meal.get_json() for meal in self.meals],
            #'meal_calendars': [meal_calendar.get_json() for meal_calendar in self.meal_calendars],
            #'calendar_integrations': [calendar_integration.get_json() for calendar_integration in self.calendar_integrations],
            #'routines': [routine.get_json() for routine in self.routines]
            #'calendar':self.calendar_integrations
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def update_user_basic(self, username,email,image):
        self.username = username
        self.image=image
        self.email=email
        
        db.session.add(self)
        db.session.commit()
        return self
    def update_user_sensitive(self,budget,weight,height,prefs,fgoals, age):
        self.budget=budget
        self.weight=weight
        self.prefs=prefs
        self.height=height
        self.fgoals=fgoals
        self.age=age
        db.session.add(self)
        db.session.commit()
        return self
        
   



