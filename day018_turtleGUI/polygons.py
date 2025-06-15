import turtle as tt
from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.bgcolor("#E0FFFF")
tt.colormode(255)
tim = Turtle()
tim.hideturtle()
tim.penup()
tim.goto(0, 300)
tim.showturtle()
tim.pendown()
tim.pensize(1)
tim.speed(0)
init_x, init_y = tim.pos()


def random_color():
    r = randint(0, 255)
    b = randint(0, 255)
    g = randint(0, 255)
    return (r, b, g)


def draw_polygon(num_sds):
    while True:
        tim.forward(20)
        tim.right(360 / num_sds)
        curr_x, curr_y = tim.pos()
        if round(curr_x, 2) == round(init_x, 2) and round(curr_y, 2) == round(
            init_y, 2
        ):
            break


for num_sides in range(3, 100):
    tim.pencolor(random_color())
    draw_polygon(num_sds=num_sides)

screen.exitonclick()
