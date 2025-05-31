class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __gt__(self, other):
        if isinstance(other, Player):
            return self.level > other.level

    def __str__(self):
        return f"{self.name}, {self.level}"


leo = Player("LEO", 30)
john = Player("JOHN", 1)
print(leo)
print(john)
print(f"leo.level > john.level : {leo > john}")
