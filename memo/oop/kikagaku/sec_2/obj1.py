# 継承
class Player:
    def __init__(self, level, name, hp, mp):
        self.level = level
        self.name = name
        self.hp = hp
        self.mp = mp

    def attack(self):
        print("敵を攻撃する。")

    def show(self):
        print(f"level: {self.level}\nname: {self.name}\nhp: {self.hp}\nmp: {self.mp}")


class Hero(Player):
    def encourage(self):
        print("みんなを勇気づける。")


john = Player(1, "John", 20, 0)
john.attack()
john.show()
# john.encourage()

leo = Hero(1, "Leo", 20, 0)
leo.attack()
leo.show()
leo.encourage()
