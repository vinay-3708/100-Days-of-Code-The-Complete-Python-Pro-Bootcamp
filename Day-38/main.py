import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 84
HEIGHT_CM = 176
AGE = 27

U_NAME = "vny-3708"
PSS = "dfgfgfthsrtart"

header = {
    "Authorization" : "Basic XXXXXXXXXXXXXXXXX"
}


APP_ID = "XXXXXXXXXXXXXX"
API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXX"
NUTRIONIX_EP = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_API_END_POINT = "https://api.sheety.co/0f2f51025b6a4d673d3dc38b9e42e3c5/tracker1/sheet1"

USER_INPUT = input("Tell me what did you do today? : ")

n_body = {
    "query" : USER_INPUT,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

n_headers = {
    'x-app-id': APP_ID,
    'x-app-key' : API_KEY
}

response = requests.post(url=NUTRIONIX_EP, headers=n_headers, json=n_body)
response.raise_for_status()
result = response.json()
print(response.json()['exercises'])


Number_of_Tasks = len(response.json()['exercises'])
print(Number_of_Tasks)
for task in range(Number_of_Tasks):
    TASK = response.json()['exercises'][task]['name'].title()
    DURATION = response.json()['exercises'][task]['duration_min']
    CALORIES = response.json()['exercises'][task]['nf_calories']
    TODAY_DATE = datetime.now().strftime("%d/%m/%Y")
    TODAY_TIME = datetime.now().strftime("%H:%M:%S")
    sheety = {
    "sheet1" : {
        "date" : TODAY_DATE,
        "time" : TODAY_TIME,
        "exercise" : TASK,
        "duration" : DURATION,
        "calories" : CALORIES
        }
    }
    response_sheety = requests.post(url=SHEETY_API_END_POINT, json=sheety)
    response_sheety.raise_for_status()
    print(response_sheety.json())   

