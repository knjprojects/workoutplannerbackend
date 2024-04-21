from flask import Blueprint, render_template, jsonify, request, flash, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user, unset_jwt_cookies, set_access_cookies
from App.controllers import get_all_users, get_user_by_username
from.index import index_views,index_page

from App.controllers import (
    login,create_user
)

auth_views = Blueprint('auth_views', __name__, template_folder='../templates')


'''
Page/Action Routes
'''    
@auth_views.route('/users', methods=['GET'])
def get_user_page():
    users = get_all_users()
    return render_template('users.html', users=users)

@auth_views.route('/identify', methods=['GET'])
@jwt_required()
def identify_page():
    return render_template('message.html', title="Identify", message=f"You are logged in as {current_user.id} - {current_user.username}")
    

@auth_views.route('/login', methods=['POST'])
def login_action():
    try:
        data = request.form
        token = login(data['username'], data['password'])
        if not token: 
            return jsonify({})
        user=get_user_by_username(data['username'])
        if user is None:
            return jsonify({}), 404
        return jsonify(user)
    except KeyError as e:
        return jsonify(error=str(e)), 400

    except Exception as e:
        return jsonify(error=str(e)), 500


@auth_views.route('/logout', methods=['GET'])
def logout_action():
    response = redirect(request.referrer) 
    flash("Logged Out!")
    unset_jwt_cookies(response)
    return response

@auth_views.route('/signup', methods=['POST'])
def signup_action():
  try:
    data = request.form  # get data from form submission
    response=None
    usa=create_user(data['username'], data['password'])
    token = login(data['username'], data['password'])
    if not token: 
        return jsonify({})
    user=get_user_by_username(data['username'])
    if user is None:
        return jsonify({}), 404
    return jsonify(user)
  except KeyError as e:
    return jsonify(error=str(e)), 400

  except Exception as e:
    return jsonify(error=str(e)), 500

'''
API Routes
'''

@auth_views.route('/api/login', methods=['POST'])
def user_login_api():
  data = request.json
  token = login(data['username'], data['password'])
  if not token:
    return jsonify(message='bad username or password given'), 401
  response = jsonify(access_token=token) 
  set_access_cookies(response, token)
  return response

@auth_views.route('/api/identify', methods=['GET'])
@jwt_required()
def identify_user():
    return jsonify({'message': f"username: {current_user.username}, id : {current_user.id}"})

@auth_views.route('/api/logout', methods=['GET'])
def logout_api():
    response = jsonify(message="Logged Out!")
    unset_jwt_cookies(response)
    return response