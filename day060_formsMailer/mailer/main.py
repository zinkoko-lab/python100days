import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect
import requests
from email.mime.text import MIMEText
from email.header import Header
import smtplib

# Load environment variables
load_dotenv()
SENDER_EMAIL = os.getenv("EMAIL_ADDRESS")
RECEIVER_EMAIL = SENDER_EMAIL
PASSWORD = os.getenv("EMAIL_PASSWORD")

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/ae1683207ec11a17b21d").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html")
    elif request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        message = request.form.get("message")

        # make a mail object
        content = f"Name:{name}\nEmail:{email}\nPhone:{phone}\nMessage:{message}"
        subject = "New Message from Blog Reader"
        msg = MIMEText(content, "plain", "utf-8")
        msg["Subject"] = Header(subject, "utf-8")
        msg["From"] = SENDER_EMAIL
        msg["To"] = RECEIVER_EMAIL

        # Send the letter generated above that person's email address.
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=SENDER_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=SENDER_EMAIL,
                to_addrs=RECEIVER_EMAIL,
                msg=msg.as_string(),
        )
        success = "Successfully sent your message"
        return render_template("contact.html", success=success)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)