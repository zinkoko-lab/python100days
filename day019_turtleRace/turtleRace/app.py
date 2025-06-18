from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=1000, height=400)
screen.bgcolor("#E0FFFF")
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
x = -(500 - 20)
y = list(range(-125, 126, 50))

for i in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.speed(3)
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x, y[i])
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > (500 - 20):
            is_race_on = False
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                result = f"You've won! The {winner_color} turtle is the winner."
            else:
                result = f"You've lose! The {winner_color} turtle is the winner."
        rand_dist = randint(0, 10)
        turtle.forward(rand_dist)

declarer = Turtle()
declarer.hideturtle()
declarer.write(result, align="center", font=("Arial", 20, "normal"))

screen.exitonclick()
