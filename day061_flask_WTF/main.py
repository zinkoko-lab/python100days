from flask import Flask, render_template, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import os

SECRET_KEY = os.urandom(24)

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField("Log In")


app = Flask(__name__)
app.secret_key = SECRET_KEY

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if request.method == "GET":
        return render_template("login.html", form=login_form)
    elif request.method == "POST":
        if login_form.validate_on_submit():
            return redirect("/")
        else:
            return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
