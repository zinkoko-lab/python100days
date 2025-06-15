import turtle as tt
from turtle import Turtle, Screen
from random import randint, choice

screen = Screen()
screen.bgcolor("#E0FFFF")

tt.colormode(255)
tim = Turtle()
tim.speed("fastest")
radius = 100


def random_color():
    r = randint(0, 255)
    b = randint(0, 255)
    g = randint(0, 255)
    return (r, b, g)


def draw_spirograph(num_circles):
    for cir_no in range(num_circles):
        tim.pencolor(random_color())
        angle = (360 / num_circles) * cir_no
        tim.setheading(angle)
        tim.circle(radius)


draw_spirograph(num_circles=100)
screen.exitonclick()
