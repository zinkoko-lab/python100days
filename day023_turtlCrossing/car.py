from random import randint
from turtle import Turtle

FINISH_LINE_Y = -320
MAX_X = 500
MIN_X = -500
MAX_Y = 250
MIN_Y = -250
REASSIGN_X = 310


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.setheading(180)
        self.initialize_randm_cor()

    def move(self, move_increment):
        self.forward(move_increment)
        if self.xcor() < MIN_X:
            self.reset_position()

    def initialize_randm_cor(self):
        init_x = randint(MIN_X, MAX_X)
        init_y = randint(MIN_Y, MAX_Y)
        self.goto(init_x, init_y)

    def reset_position(self):
        new_x = REASSIGN_X
        new_y = randint(MIN_Y, MAX_Y)
        self.goto(new_x, new_y)
