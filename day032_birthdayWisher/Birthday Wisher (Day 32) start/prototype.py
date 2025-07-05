import smtplib

with open(file="mail_account.txt") as f:
    data = f.readlines()
sender_email = data[0].strip()
password = data[1].strip()
receiver_email = data[2].strip()


with smtplib.SMTP("smtp.gmail.com") as connection:
    # TLS (Transport Layer Security) を有効にする(盗聴等のセキュリティー対策)
    connection.starttls()
    connection.login(user=sender_email, password=password)
    connection.sendmail(
        from_addr=sender_email,
        to_addrs=receiver_email,
        msg="Subject:Hello\n\nThis is the body of my email.",
    )
