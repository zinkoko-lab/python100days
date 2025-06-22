from turtle import Turtle

FONT = ("Courier New", 80, "normal")
ALLIGNMENT = "center"
COLOR = "white"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color(COLOR)
        self.penup()
        self.hideturtle()
        self.__l_score = 0
        self.__r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.__l_score, align=ALLIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.__r_score, align=ALLIGNMENT, font=FONT)

    def increase_l_score(self):
        self.__l_score += 1
        self.update_score()

    def increase_r_score(self):
        self.__r_score += 1
        self.update_score()
