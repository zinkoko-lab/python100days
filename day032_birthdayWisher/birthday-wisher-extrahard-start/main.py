import smtplib
import os
from dotenv import load_dotenv
from random import choice
import datetime as dt

# import pytz
from email.mime.text import MIMEText
from email.header import Header
import pandas as pd

# Load environment variables
load_dotenv()
SENDER_EMAIL = os.getenv("EMAIL_ADDRESS")
PASSWORD = os.getenv("EMAIL_PASSWORD")


# Check if today matches a birthday in the birthdays.csv
df = pd.read_csv("birthdays.csv")
people_list = df.to_dict(orient="records")
# utc_now = dt.datetime.now(pytz.utc)
# tokyo_tz = pytz.timezone("Asia/Tokyo")
# tokyo_now = utc_now.astimezone(tokyo_tz)
# tokyo_today = tokyo_now.day
# current_month = tokyo_now.month
now = dt.datetime.now()
today = now.day
current_month = now.month
today_birthday_people = []
for person in people_list:
    someone_birth_day = person["day"]
    someone_birth_month = person["month"]
    if someone_birth_day == today and someone_birth_month == current_month:
        today_birthday_people.append(person)


# If anyone's birthday is today, pick a random letter from letter templates
# and replace the [NAME] with the person's actual name from birthdays.csv
if len(today_birthday_people) > 0:

    for person in today_birthday_people:
        name = person["name"]
        receiver_email = person["email"]

        with open(file=f"./letter_templates/letter_{choice(range(1,4))}.txt") as f:
            text = f.read()

        subject = "Happy Birthday!"
        message = text.replace("[NAME]", name)

        # make a mail object
        msg = MIMEText(message, "plain", "utf-8")
        msg["Subject"] = Header(subject, "utf-8")
        msg["From"] = SENDER_EMAIL
        msg["To"] = receiver_email

        # Send the letter generated above that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=SENDER_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=SENDER_EMAIL,
                to_addrs=receiver_email,
                msg=msg.as_string(),
            )
