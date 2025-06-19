from turtle import Turtle

ALLIGNMENT = "center"
FONT = ("Courier New", 20, "normal")
LOCATION = (0, 275)


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.__score = 0
        self.hideturtle()
        self.pencolor("white")
        self.speed("fastest")
        self.penup()
        self.goto(LOCATION)
        self.pendown()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(
            f"Score : {self.__score}",
            align=ALLIGNMENT,
            font=FONT,
        )

    def game_over(self):
        self.home()
        self.write(
            "GAME OVER\nPress 'R' to restart\nor click on screen to exit",
            align=ALLIGNMENT,
            font=FONT,
        )

    def increase_score(self):
        self.__score += 1
        self.clear()
        self.update_scoreboard()
