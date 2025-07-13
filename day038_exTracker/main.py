from dotenv import load_dotenv
import os
import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth

load_dotenv()
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
SHEET_END_PT = os.getenv("SHEET_END_PT")
SHEET_BASIC_USER = os.getenv("SHEET_BASIC_USER")
SHEET_BASIC_PASS = os.getenv("SHEET_BASIC_PASS")

endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
}

exercise_you_did = input("Tell me which exercises you did: ")

params = {
    "query": exercise_you_did,
}

response = requests.post(url=endpoint, headers=headers, json=params)

exercises_list = response.json()["exercises"]
now = datetime.now()
DATE = now.strftime("%d/%m/%Y")
TIME = now.strftime("%H:%M:%S")
basic = HTTPBasicAuth(username=SHEET_BASIC_USER, password=SHEET_BASIC_PASS)


for data in exercises_list:
    exercise = data["name"].title()
    duration = data["duration_min"]
    calories = data["nf_calories"]
    params = {
        "workout": {
            "date": DATE,
            "time": TIME,
            "exercise": exercise,
            "duration": duration,
            "calories": calories,
        }
    }

    response = requests.post(url=SHEET_END_PT, json=params, auth=basic)
    print(response.text)
