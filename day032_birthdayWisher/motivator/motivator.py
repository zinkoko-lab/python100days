import smtplib
import os
from dotenv import load_dotenv
from random import choice
import datetime as dt
from email.mime.text import MIMEText
from email.header import Header


weekday_of_today = dt.datetime.now().weekday()
if weekday_of_today == 0:
    # .envファイルを読み込む
    load_dotenv()

    # 環境変数から値を取得
    sender_email = os.getenv("EMAIL_ADDRESS")
    password = os.getenv("EMAIL_PASSWORD")
    receiver_email = sender_email

    # quotesの中身を読み込む
    with open(file="quotes.txt") as f:
        data = f.readlines()
        quotes = [quote.strip().split("-") for quote in data]

    subject = "Vitamin Quote to Me"

    # Generate a Random Quote
    today_quote = choice(quotes)

    # 本文
    message = today_quote[0]

    # 署名
    signature = "---" + "\n" + today_quote[1]

    # メール本文 + 署名を結合
    full_message = f"{message}\n{signature}"

    # メールオブジェクトの作成
    msg = MIMEText(full_message, "plain", "utf-8")
    msg["Subject"] = Header(subject, "utf-8")
    msg["From"] = sender_email
    msg["To"] = receiver_email

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password)
        connection.sendmail(
            from_addr=sender_email,
            to_addrs=receiver_email,
            msg=msg.as_string(),
        )
