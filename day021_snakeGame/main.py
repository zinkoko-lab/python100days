from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


def play_game():
    snake = Snake()
    food = Food()
    scoreboard = ScoreBoard()

    screen.listen()
    screen.onkey(key="Up", fun=snake.up)
    screen.onkey(key="Down", fun=snake.down)
    screen.onkey(key="Right", fun=snake.right)
    screen.onkey(key="Left", fun=snake.left)

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # 食べ物との衝突
        if snake.head.distance(food) < 15:
            snake.extend()
            food.refresh()
            scoreboard.increase_score()

        # 壁との衝突
        if (
            snake.head.xcor() > 280
            or snake.head.xcor() < -280
            or snake.head.ycor() > 280
            or snake.head.ycor() < -280
        ):
            game_is_on = False
            scoreboard.game_over()

        # 自分の体との衝突
        for seg in snake.segments[1:]:
            if snake.head.distance(seg) < 10:
                game_is_on = False
                scoreboard.game_over()

    # 再スタートの待ち受け
    screen.onkey(lambda: restart_game(), "r")


def restart_game():
    screen.clear()
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.setup(width=600, height=600)
    screen.tracer(0)
    play_game()


# 最初のゲーム開始
play_game()

screen.listen()
screen.exitonclick()
