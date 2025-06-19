import turtle

screen = turtle.Screen()
pen = turtle.Turtle()
pen.hideturtle()

# Move the turtle to (100, 50)
pen.penup()
pen.goto(0, 200)
pen.pendown()

# Write text at the current position
pen.write("Hello, World!", align="center", font=("Arial", 16, "normal"))

screen.exitonclick()
