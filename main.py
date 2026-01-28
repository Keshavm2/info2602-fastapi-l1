from fastapi import FastAPI
import json

app = FastAPI()

global data

with open('./data.json') as f:
    data = json.load(f)


@app.get('/')
def hello_world():
    return 'Hello, World!'

@app.get('/students')
async def get_students(pref=None):
    if pref:
        filtered_students = []
        for student in data:
            if student['pref'] == pref: 
                filtered_students.append(student) 
        return filtered_students
    return data

@app.get('/students/{id}')
async def get_student(id):
  for student in data: 
    if student['id'] == id: 
      return student
    
@app.get('/stats')
async def get_stats():
    mealCount = {}
    programCount = {}

    for student in data:
        pref = student['pref']
        if pref in mealCount:
            mealCount[pref] += 1
        else:
            mealCount[pref] = 1
            
        
        programme = student['programme']
        if programme in programCount:
            programCount[programme] += 1
        else:
            programCount[programme] = 1
    
    return mealCount, programCount

@app.get('/add/{a}/{b}')
async def add(a, b):
    a = float(a)
    b = float(b)
    return a + b

@app.get('/subtract/{a}/{b}')
async def subtract(a, b):
    a = float(a)
    b = float(b)
    return a - b

@app.get('/multiply/{a}/{b}')
async def multiply(a, b):
    a = float(a)
    b = float(b)
    return a * b

@app.get('/divide/{a}/{b}')
async def divide(a, b):
    a = float(a)
    b = float(b)
    return a / b