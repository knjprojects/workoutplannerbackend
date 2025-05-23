import csv
from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.database import db
from App.controllers import create_user,create_test_users
#createRoutine,createMeal,getMeals,mealsForUser,getFoodById,createCalendar,get_user_calendars,createMealCalendarEntry, getMealCalendarEntryForUser,createRoutineCalendarEntry,list_cals,removeMeal,getAllMealCalendars,getAllRoutineCalendars,addExerciseToRoutine
from App.controllers import login#,loadExercises,loadFoods,list_foods,list_exercises,list_routines,get_user_routines
index_views = Blueprint('index_views', __name__)


#did not return json for meal and calendar to test functions, may have to do the same, or not for other controllers

@index_views.route('/', methods=['GET'])
def index_page():
    db.drop_all()
    db.create_all()
    user1=create_test_users()
    #create_book('The Hobbit', 'J.R.R. Tolkien', 'George Allen & Unwin','https://m.media-amazon.com/images/M/MV5BMzU0NDY0NDEzNV5BMl5BanBnXkFtZTgwOTIxNDU1MDE@._V1_FMjpg_UX1000_.jpg')
    #loadExercises()
    #loadFoods()
    #if user1:
        #user1.review_book(1, 3,'A great book!')
        #userid=user1.id
        #createRoutine(user1.id, 'Abs Workout', 'I want to build abs', "['Meat', 'Veggies']","['Weight Loss', 'Building Muscle']")
        #meal=createMeal(user1.id,1)
        #cal=createCalendar(date='04-12-2016',user_id=user1.id,timezone='AST')
            
            #return jsonify(cal2.get_json())
        #mcel=createMealCalendarEntry(user_id=user1.id,meal_id=1,calendar_integration_id=cal.id,date='04-12-2016',time='allday')
        #user2=create_user(username='jake', email='jake@example.com', password='jakepass',budget=300,gender='female',age=30,weight=200,height="1.564")
        #if user2:
            #meal2=createMeal(user2.id,5)
            #cal2=createCalendar(date='04-12-2016',user_id=user2.id,timezone='AST')
            #rout=createRoutine(user2.id, 'Legs Workout', 'I want toworkout my quadriceps', "['Milk', 'Fish']","['Endurance', 'Building Muscle']")
            #crcel=createRoutineCalendarEntry(date='04-12-2016',user_id=user2.id,routine_id=rout.id,calendar_integration_id=cal2.id,time='allday')
            #mcel2=createMealCalendarEntry(user_id=user2.id,meal_id=2,calendar_integration_id=cal2.id,date='04-12-2016',time='allday')
            #return jsonify(crcel)
        #return jsonify(message='Did not create cal or mcel?')
        #prefs="", fgoals=""
    
    return render_template('index.html')

"""def createWorkDay(date,time,rout,meal,user_id,cal): 
    createRoutineCalendarEntry(date=date,user_id=user_id,routine_id=rout,calendar_integration_id=cal,time=time)
    tried=createMealCalendarEntry(user_id=user_id,meal_id=meal,calendar_integration_id=cal,date=date,time=time)
    if tried:
        return True
    return None
"""
@index_views.route('/init', methods=['GET'])
def init():
    db.drop_all()
    db.create_all()
    
    user1=create_test_users()
    #create_book('The Hobbit', 'J.R.R. Tolkien', 'George Allen & Unwin','https://m.media-amazon.com/images/M/MV5BMzU0NDY0NDEzNV5BMl5BanBnXkFtZTgwOTIxNDU1MDE@._V1_FMjpg_UX1000_.jpg')
    #loadExercises()
    #loadFoods()
    #if user1:
        #user1.review_book(1, 3,'A great book!')
        #userid=user1.id
        #createRoutine(user1.id, 'Abs Workout', 'I want to build abs', "['Meat', 'Veggies']","['Weight Loss', 'Building Muscle']")
        #meal=createMeal(user1.id,1)
        #cal=createCalendar(date='04-12-2016',user_id=user1.id,timezone='AST')
            
            #return jsonify(cal2.get_json())
       # mcel=createMealCalendarEntry(user_id=user1.id,meal_id=1,calendar_integration_id=cal.id,date='04-12-2016',time='allday')
        #user2=create_user(username='jake', email='jake@example.com', password='jakepass',budget=300,gender='female',age=30,weight=200,height="1.564")
        #if user2:
           # meal2=createMeal(user2.id,5)
           # cal2=createCalendar(date='04-12-2016',user_id=user2.id,timezone='AST')
           # rout=createRoutine(user2.id, 'Legs Workout', 'I want toworkout my quadriceps', "['Milk', 'Fish']","['Endurance', 'Building Muscle']")
           # crcel=createRoutineCalendarEntry(date='04-12-2016',user_id=user2.id,routine_id=rout.id,calendar_integration_id=cal2.id,time='allday')
           # mcel2=createMealCalendarEntry(user_id=user2.id,meal_id=2,calendar_integration_id=cal2.id,date='04-12-2016',time='allday')
    return jsonify(message='db initialized!')
# list all exercises
@index_views.route('/exercises', methods=['GET'])
def exercises():

    return jsonify("printing exercises")#listexercises
#
"""
@index_views.route('/foods', methods=['GET'])
def foods():
    return jsonify(list_foods())
#

@index_views.route('/foods<int:food_id>', methods=['GET'])
def foodsById(food_id):
    return jsonify(getFoodById(foodid=food_id))
#

#list all users routines, should have one listing routines for a specific user
@index_views.route('/routines', methods=['GET'])
def routines():
    return jsonify(list_routines())

@index_views.route('/routines/<int:user_id>', methods=['GET'])
def user_routines(user_id):
    return jsonify(get_user_routines(user_id=user_id))


@index_views.route('/meals', methods=['GET'])
def meals():
    return jsonify(getMeals())

@index_views.route('/meals/<int:user_id>', methods=['GET'])
def user_meals(user_id):
    return jsonify(mealsForUser(user_id=user_id))

@index_views.route('/meals/remove', methods=['POST'])
def remove_meal():
    data=request.form
    rem=removeMeal(meal_id=data['meal_id'])
    if rem:
        return jsonify(message='Meal removed from user')
    return jsonify(message='Failed')

@index_views.route('/calendars', methods=['GET'])
def calendars():
    cals=list_cals()
    return jsonify(cals)

@index_views.route('/calendars/<int:user_id>', methods=['GET'])
def user_calendars(user_id):
    usercals=get_user_calendars(user_id=user_id)
    return jsonify(usercals)


@index_views.route('/mealcalendars', methods=['GET'])
def meal_calendars():
    mealcals=getAllMealCalendars()
    #mealcal=getMealCalendarEntryForUser(user_id=1, date='04-12-2016.8:30',calendar_id=1)
    return jsonify(mealcals)


@index_views.route('/routinecalendars', methods=['GET'])
def routine_calendars():
    routinecal=getAllRoutineCalendars()
    return jsonify(routinecal)

@index_views.route('/calendars/createMealandRout', methods=['POST'])
def createWorkDay():
    data=request.form
    #date: date,time: time,rout:rout,meal:meal
    workday=createWorkDay(user_id=data['user_id'],date=data['date'],time=data['time'],rout=data['rout'],meal=data['meal'],cal=data['cal'])
    if workday:
        return jsonify(message="Done")
    return jsonify(message="Fail")

@index_views.route('/addExerciseToRoutine', methods=['POST'])
def createExerciseRoutine():
    data=request.form
    ex=addExerciseToRoutine(routine_id=data['rout'],exercise_id=data['exer'])
    if ex:
        return jsonify(ex)
    return jsonify(message="Fail")

"""
@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})

"""@index_views.route('/api/data')
def get_data():
    response = index_views.open('https://amiiboapi.com/api/amiibo/?showusage').json()#requests.get('https://amiiboapi.com/api/amiibo/?showusage')
    data = response.json()
    return jsonify(data.amiibo)
    """

