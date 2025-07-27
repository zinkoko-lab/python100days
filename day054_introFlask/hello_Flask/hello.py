from flask import Flask
from markupsafe import escape

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        text = function()
        return f"<b>{text}</b>"

    return wrapper


def make_emphasis(function):
    def wrapper():
        text = function()
        return f"<em>{text}</em>"

    return wrapper


def make_underlined(function):
    def wrapper():
        text = function()
        return f"<u>{text}</u>"

    return wrapper


@app.route("/")
def hello_world():
    return (
        '<h1 style="text-align: center"">Hello, World!</h1>'
        "<p>This is a paragraph.</p>"
        '<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExZzRrZWh0ZDl3MDgxaGRuaHc5MXY3bDhyNTFzYTRiNjVjMHhyYnR0biZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/5exwXWg9u7yow/giphy.gif" width=200 />'
    )


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "<p>Bye!</p>"


@app.route("/username/<name>/<age>")
def hello(name, age):
    return f"<p>Hello there, {name}. You are {age} years old!</p>"


if __name__ == "__main__":
    app.run(debug=True)
