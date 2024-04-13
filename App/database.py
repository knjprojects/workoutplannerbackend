from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def get_migrate(app):
    return Migrate(app, db)

def create_db():
    db.create_all()
    
def init_db(app):#called in main.py
    db.init_app(app)