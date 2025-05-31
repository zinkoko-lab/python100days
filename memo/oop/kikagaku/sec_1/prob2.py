class Car:
    def __init__(self, color):
        self.color = color

    def print_color(self):
        print(f"{self.color}色の車です。")

    def run(self):
        print("発進します!")


red_car = Car("赤")
red_car.print_color()
red_car.run()
