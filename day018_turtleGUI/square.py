from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("#E0FFFF")
timmy_the_turtle = Turtle()
timmy_the_turtle.pensize(3)
timmy_the_turtle.speed(1)
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
ix, iy = timmy_the_turtle.pos()
while True:
    timmy_the_turtle.forward(200)
    timmy_the_turtle.left(90)
    cx, cy = timmy_the_turtle.pos()
    if round(cx, 2) == round(ix, 2) and round(cy, 2) == round(iy, 2):
        break

screen.exitonclick()
