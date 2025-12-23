# Level-3: Inheritance
# Implementing inheritance


class Animal:

    def sound(self):
        print("Some sound")


class Dog(Animal):

    def sound(self):
        print("Woof!")


my_dog = Dog()
my_dog.sound()
