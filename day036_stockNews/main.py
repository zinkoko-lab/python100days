import requests
import os
from dotenv import load_dotenv
from pprint import pprint
from datetime import datetime, timedelta
from twilio.rest import Client

load_dotenv()
ALPHA_API_KEY = os.getenv("ALPHA_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

TWILIO_PH_NO = os.getenv("TWILIO_PH_NO")
MY_PN_NO = os.getenv("MY_PN_NO")

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHA_API_KEY,
}
response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
stock_data = response.json()["Time Series (Daily)"]
stock_data_list = [value for (key, value) in stock_data.items()]
recent_two_day_data = stock_data_list[:2]
yesterday_data = recent_two_day_data[0]
before_yesterday_data = recent_two_day_data[1]
yesterday_close_price = float(yesterday_data["4. close"])
before_yesterday_close_price = float(before_yesterday_data["4. close"])
difference = yesterday_close_price - before_yesterday_close_price
diff_percentage = round((abs(difference) / yesterday_close_price) * 100, 2)

if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

if diff_percentage > 5:
    today = datetime.today().date()
    yesterday = str(today - timedelta(days=1))
    news_params = {
        "q": COMPANY_NAME,
        "language": "en",
        "from": yesterday,
        "to": yesterday,
        "apiKey": NEWS_API_KEY,
    }
    response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    first_three_articles = response.json()["articles"][:3]

    # Send a separate message with each article's title and description to your phone number.

    client = Client(account_sid=TWILIO_ACCOUNT_SID, password=TWILIO_AUTH_TOKEN)
    for article in first_three_articles:
        text = f"{STOCK}: {up_down}{diff_percentage}%\nHeadline:{article["title"]}"
        message = client.messages.create(
            body=text,
            from_=TWILIO_PH_NO,
            to=MY_PN_NO,
        )
        print(message.body)
