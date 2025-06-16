import turtle as tt
from turtle import Turtle, Screen
from colors import color_list
from random import choice

screen = Screen()
screen.bgcolor("#E0FFFF")

tt.colormode(255)
tim = Turtle()
tim.hideturtle()
tim.penup()
tim.goto(-300, -250)
tim.speed(3)
x = list(range(-250, 251, 50))
y = x
coordinates = []
for j in y:
    for i in x:
        coordinates.append((i, j))

for coord in coordinates:
    tim.goto(coord)
    tim.dot(20, choice(color_list))


screen.exitonclick()
