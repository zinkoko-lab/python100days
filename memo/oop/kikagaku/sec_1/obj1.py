class Player:
    def __init__(self, level, name):
        self.level = level
        self.name = name

    def attack(self):
        print("敵を攻撃する。")

    def show(self):
        print(f"level: {self.level}, name: {self.name}")


player_1 = Player(5, "JIN")
player_1.show()
player_1.attack()
