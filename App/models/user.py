from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

"""class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False, unique=True)
    email =  db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    gender = db.Column(db.String(120), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    weight= db.Column(db.Integer, nullable=False)
    height= db.Column(db.String(100), nullable=False)



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
       
        self.password = generate_password_hash(password)

    def check_password(self, password):
       
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
        
    # to svoifd circular import issue on render, im importing it using a lazy import instead top of the file
    """
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    recipes = db.relationship('Recipe', backref='author', lazy=True)
    password_hash = db.Column(db.String(128))
    ingredients = db.Column(db.Text, nullable=True)  # Comma-separated list of ingredient names
    comments = db.relationship('Comment', backref='author', lazy=True)

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def remove_recipe(self, recipe):
        self.recipes.remove(recipe)

    def find_recipes(self):
        """Find recipes that can be made with the user's ingredients."""
        if not self.ingredients:
            return []
        user_ingredients = set(self.ingredients.split(','))
        return Recipe.query.filter(
            Recipe.ingredients.any(Ingredient.name.in_(user_ingredients))
        ).all()

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.username