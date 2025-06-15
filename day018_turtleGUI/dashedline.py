from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("#E0FFFF")
tim = Turtle()
tim.pensize(2)
tim.speed(1)
tim.shape("turtle")
tim.color("red")
# ix, iy = tim.pos()

for _ in range(30):
    tim.forward(5)
    tim.penup()
    tim.forward(5)
    tim.pendown()

screen.exitonclick()
