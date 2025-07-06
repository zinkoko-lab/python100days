import pytz
import requests
import datetime as dt

MY_LAT = 34.765388
MY_LONG = 137.397110

# ISS API TEST
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
print((longitude, latitude))


# SUN RISE, SUN SET API TEST
# REASON -> If the sky is actually dark enough for us to be able to spot the ISS
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid": "Asia/Tokyo",
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise.split("T")[1].split(":")[0])
print(sunset.split("T")[1].split(":")[0])

utc_now = dt.datetime.now(pytz.utc)
tokyo_tz = pytz.timezone("Asia/Tokyo")
tokyo_now = utc_now.astimezone(tokyo_tz)
print(tokyo_now.now().hour)
