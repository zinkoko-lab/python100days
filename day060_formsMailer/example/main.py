from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def receive_data():
    if request.method == "GET":
        return redirect("/")
    elif request.method == "POST":
        name = request.form.get("name")
        password = request.form.get("password")
        print(f"name: {name}\npassword:{password}")
        return f"<h1>Name:{name},Password:{password}</h1>"

if __name__ == "__main__":
    app.run(debug=True)