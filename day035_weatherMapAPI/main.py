import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client


load_dotenv()
API_KEY = os.getenv("API_KEY")
MY_LAT = float(os.getenv("MY_LAT"))
MY_LONG = float(os.getenv("MY_LONG"))
TWILIO_PH_NO = os.getenv("TWILIO_PH_NO")
MY_PN_NO = os.getenv("MY_PN_NO")

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt": 4,
}
response = requests.get(OWM_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()["list"]
weather_id_list = [data["weather"][0]["id"] for data in weather_data]


will_rain = False
for id in weather_id_list:
    if id < 700:
        will_rain = True
# at the next 12 hour forecast, is rainy?
if will_rain:
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella.☔️",
        from_=TWILIO_PH_NO,
        to=MY_PN_NO,
    )
