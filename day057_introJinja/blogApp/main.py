from flask import Flask, render_template
import requests

app = Flask(__name__)


def get_blogs():
    npoit_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(npoit_url)
    return response.json()


@app.route("/")
def home():
    blogs = get_blogs()
    return render_template("index.html", blogs=blogs)


@app.route("/post/<int:id>")
def read_post(id):
    blogs = get_blogs()
    blog = blogs[id - 1]
    return render_template("post.html", blog=blog)


if __name__ == "__main__":
    app.run(debug=True)
