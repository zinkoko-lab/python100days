from random import randint, choice
from car import Car

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:

    def __init__(self):
        self.cars = []
        self.generate_cars()
        self.move_speed = STARTING_MOVE_DISTANCE

    def generate_cars(self):
        for _ in range(20):
            new_car = Car()
            new_car.color(choice(COLORS))
            self.cars.append(new_car)

    def move_cars(self):
        for each_car in self.cars:
            each_car.move(self.move_speed)

    def speed_up(self):
        self.move_speed += MOVE_INCREMENT
