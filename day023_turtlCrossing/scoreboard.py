from turtle import Turtle

ALLIGNMENT = "center"
FONT = ("Courier", 24, "normal")
COLOR = "black"
LEVEL_TEXT_LOCATION = (-200, 270)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.level = 1
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(LEVEL_TEXT_LOCATION)
        self.write(f"level : {self.level}", align=ALLIGNMENT, font=FONT)

    def level_up(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.home()
        self.write(
            "GAME OVER\nPress 'R' to restart\nor click on screen to exit",
            align=ALLIGNMENT,
            font=FONT,
        )
