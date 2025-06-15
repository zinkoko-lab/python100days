import turtle as tt
from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.bgcolor("#E0FFFF")
tt.colormode(255)
tim = Turtle()
tim.hideturtle()
tim.penup()
tim.goto(-50, 150)
tim.showturtle()
tim.pendown()
tim.pensize(3)
tim.speed(5)
init_x, init_y = tim.pos()
for num_side in range(4, 10):
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    tim.pencolor(red, green, blue)
    while True:
        tim.forward(100)
        tim.right(360 / num_side)
        curr_x, curr_y = tim.pos()
        if round(curr_x, 2) == round(init_x, 2) and round(curr_y, 2) == round(
            init_y, 2
        ):
            break

screen.exitonclick()
