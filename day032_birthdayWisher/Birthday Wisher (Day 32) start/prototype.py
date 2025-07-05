import smtplib
import os
from dotenv import load_dotenv

# .envファイルを読み込む
load_dotenv()

# 環境変数から値を取得
sender_email = os.getenv("EMAIL_ADDRESS")
password = os.getenv("EMAIL_PASSWORD")
receiver_email = os.getenv("RECEIVER_EMAIL")

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=sender_email, password=password)
    connection.sendmail(
        from_addr=sender_email,
        to_addrs=receiver_email,
        msg="Subject:Hello\n\nThis is the body of my email.",
    )
