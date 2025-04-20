import csv
from App.models import Exercise
from App.database import db

def loadExercises():
    with open('exercises.csv', newline='', encoding='utf8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:#name,description,musclegroup,equipment,difficulty,image
            exercise = Exercise(name=row['name'],description=row['description'],muscle=row['muscle'], equipment=row['equipment'],difficulty=row['difficulty'],image=row['image'])
            db.session.add(exercise)
    db.session.commit()

def list_exercises():
    exercises=Exercise.query.all()
    if not exercises:
        return []
    exercises_list = [exercise.get_json() for exercise in exercises]
    return exercises_list

