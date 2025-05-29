class Player:
    def __init__(self, level, name):
        self.level = level
        self.name = name

    def __str__(self):
        return "{} {} ".format(self.level, self.name)

def print_message():
    print("Hello")

def echo_message(message):
    print(message)
