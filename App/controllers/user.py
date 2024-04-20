from flask import jsonify
from App.models import User
from App.database import db

def create_user(username, password,email, budget,gender,age,weight,height):
    newuser = User(username=username, password=password,email=email,budget=budget,gender=gender,age=age,weight=weight,height=height)
    try:
        db.session.add(newuser)
        db.session.commit()  # save user
        return newuser
        
    except Exception:  # attempted to insert a duplicate user
        db.session.rollback()
        # error message
    return None

def get_user_by_username(username):
    usa=User.query.filter_by(username=username).first()
    user=usa.get_json()
    return user

def get_user(id):
    return User.query.get(id)

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users

def delete_user( username):
    user =get_user_by_username(username)
    if user:
      try:
        db.session.delete(user)
        db.session.commit()
        return True
      except Exception:  # database error
        db.session.rollback()
    return None # user does not exist

def create_test_users():#,bobpass,200,"['Meat', 'Veggies']","['Weight Loss', 'Building Muscle']"
    user1 = create_user(username='bob', email='bob@example.com', password='bobpass',budget=200,gender='male',age=21,weight=120,height="1.8796")
    return user1