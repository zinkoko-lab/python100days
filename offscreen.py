import turtle
import random

screen_width = 600
screen_height = 400
screen = turtle.Screen()
screen.setup(width=screen_width, height=screen_height)
screen.bgcolor("light green")
screen.title("Turtle Boundary Example")

pen = turtle.Turtle()
pen.shape("turtle")
pen.color("blue")
pen.speed(0)


def is_off_screen(x, y, width, height):
    """Checks if a point is outside the screen boundaries."""
    return abs(x) > width / 2 or abs(y) > height / 2


def move_and_bounce():
    """Moves the turtle and handles boundary collisions."""
    x, y = pen.position()
    dx = random.randint(-10, 10)
    dy = random.randint(-10, 10)
    new_x = x + dx
    new_y = y + dy

    if is_off_screen(new_x, new_y, screen_width, screen_height):
        pen.setx(x - dx)  # Reverse direction
        pen.sety(y - dy)
    else:
        pen.goto(new_x, new_y)
    screen.ontimer(move_and_bounce, 100)  # Adjust delay for speed


move_and_bounce()  # Start the movement loop
screen.mainloop()
