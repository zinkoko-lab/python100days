import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("The turtle is crossing the road")
screen.tracer(0)


def turtle_crossing_game():
    player = Player()
    carman = CarManager()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(key="Up", fun=player.cross_road)

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()

        carman.move_cars()

        for each_car in carman.cars:
            if player.distance(each_car) < 20:
                scoreboard.game_over()
                game_is_on = False

        if player.is_at_finish_line():
            player.reset_position()
            carman.speed_up()
            scoreboard.level_up()

    screen.onkey(key="r", fun=restart_game)


def restart_game():
    screen.clear()
    screen.setup(width=600, height=600)
    screen.tracer(0)
    turtle_crossing_game()


turtle_crossing_game()

screen.exitonclick()
