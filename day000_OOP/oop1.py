# Level-1: Creating a Class and Object
# Defining a class and creating an object


class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Car: {self.brand} {self.model}")


my_car = Car("Toyota", "Corolla")
my_car.display_info()
