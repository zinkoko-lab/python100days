from flask import Flask, render_template
from datetime import datetime, timedelta
from random import randint
import requests
from pprint import pprint

app = Flask(__name__)

@app.context_processor
def inject_now():
    return {"current_year": datetime.now().year}

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

@app.route("/")
def home():
    return render_template("index.html", blogs=blogs)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/post/<int:blog_id>")
def read_more(blog_id):
    blog = blogs[blog_id-1]
    pprint(blog)
    return render_template("post.html", blog=blog)


if __name__ == "__main__":
    app.run(debug=True)