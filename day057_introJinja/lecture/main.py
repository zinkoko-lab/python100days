from flask import Flask, render_template
from datetime import datetime
import requests

GENDERIZE_IO_URL = "https://api.genderize.io?name=peter"
app = Flask(__name__)


@app.context_processor
def inject_now():
    return {"current_year": datetime.now().year}


@app.route("/guess/<some_name>")
def guess(some_name):
    GENDERIZE_IO_URL = f"https://api.genderize.io?{some_name}"
    AGIFY_IO_URL = f"https://api.agify.io?name?{some_name}"
    genderize_response = requests.get(url=GENDERIZE_IO_URL)
    gender = genderize_response.json()["gender"]
    agify_response = requests.get(url=AGIFY_IO_URL)
    age = agify_response.json()["age"]

    return render_template("index.html", name=some_name.title(), gender=gender, age=age)


@app.route("/blog")
def blog():
    blog_url = "https://api.npoint.io/07b256cc056415727a21"
    response = requests.get(url=blog_url)
    blogs = response.json()

    return render_template("blog.html", blogs=blogs)


if __name__ == "__main__":
    app.run(debug=True)
