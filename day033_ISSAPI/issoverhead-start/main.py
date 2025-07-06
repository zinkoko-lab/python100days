import requests
from datetime import datetime
import pytz
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os
from dotenv import load_dotenv
from config import subject, body

# Load environment variables
load_dotenv()
SENDER_EMAIL = os.getenv("EMAIL_ADDRESS")
RECEIVER_EMAIL = SENDER_EMAIL
PASSWORD = os.getenv("EMAIL_PASSWORD")
MY_LAT = float(os.getenv("MY_LAT"))
MY_LONG = float(os.getenv("MY_LONG"))
SUBJECT = subject
BODY = body

# Getting current position of ISS from ISS API
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Your position is within +5 or -5 degrees of the ISS position.
def is_close_to_me():
    if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and (
        MY_LONG - 5 <= iss_longitude <= MY_LONG + 5
    ):
        return True


# the sky is actually dark enough for your location to be able to spot the ISS or not.
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid": "Asia/Tokyo",
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

utc_now = datetime.now(pytz.utc)
jst = pytz.timezone("Asia/Tokyo")
jst_now = utc_now.astimezone(jst)
now = jst_now.hour


def is_dark_now():
    if now < sunrise and now > sunset:
        return True


# If the ISS is close to my current position
# and it is currently dark
if is_close_to_me() and is_dark_now():

    # make a mail object
    msg = MIMEText(BODY, "plain", "utf-8")
    msg["Subject"] = Header(SUBJECT, "utf-8")
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL

    # Then send me an email to tell me to look up.
    # Send the letter generated above that person's email address.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=SENDER_EMAIL,
            to_addrs=RECEIVER_EMAIL,
            msg=msg.as_string(),
        )

# BONUS: run the code every 60 seconds.
