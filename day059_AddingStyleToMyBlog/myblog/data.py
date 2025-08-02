import requests
from pprint import pprint
from datetime import datetime, timedelta
from random import randint


def generate_random_date_str(today: datetime):
    max_days = 10
    start_date = today - timedelta(days=-max_days)
    random_num_days = randint(0, max_days)
    random_datetime = start_date + timedelta(days=random_num_days)
    return random_datetime.strftime("%B %d, %Y")

response = requests.get("https://api.npoint.io/ae1683207ec11a17b21d")
blogs = response.json()

today = datetime.now()
for blog in blogs:
    blog["date"] = generate_random_date_str(today=today)


blogs = blogs