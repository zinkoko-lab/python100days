import turtle as tt
from turtle import Turtle, Screen
from random import randint, choice

screen = Screen()
screen.bgcolor("#E0FFFF")
tt.colormode(255)
tim = Turtle()
tim.hideturtle()
tim.penup()
tim.goto(-50, 150)
tim.showturtle()
tim.pendown()
tim.pensize(10)
tim.speed(0)
directions = [0, 90, 180, 270]


def random_color():
    r = randint(0, 255)
    b = randint(0, 255)
    g = randint(0, 255)
    return (r, b, g)


def random_walk():
    tim.forward(30)
    tim.setheading(choice(directions))


for _ in range(1000):
    tim.pencolor(random_color())
    random_walk()

screen.exitonclick()
