from App.models import User
from App.database import db

def create_user(username, password):
    newuser = User(username=username, password=password)
    db.session.add(newuser)
    db.session.commit()
    return newuser

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

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


def signUpUser(username,password):
    newuser = create_user(username=username,
                      
                        password=password)  # create user object
    
    try:
        db.session.add(newuser)
        db.session.commit()  # save user
        return newuser
        
    except Exception:  # attempted to insert a duplicate user
        db.session.rollback()
        # error message
    return None