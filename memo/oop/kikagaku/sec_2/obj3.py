# 継承及びオーバーライド
# super classの　__init__()を sub class でオーバーライドしてみる
# 今度は Heroクラスに tp_rate のインスタンス変数を追加
class Player:
    def __init__(self, level, name, hp, mp):
        self.level = level
        self.name = name
        self.hp = hp
        self.mp = mp

    def attack(self):
        print(f"{self.name}が敵を攻撃する。")

    def show(self):
        print(f"level: {self.level}\nname: {self.name}\nhp: {self.hp}\nmp: {self.mp}")


class Hero(Player):
    def __init__(self, level, name, hp, mp, tp_rate):
        super().__init__(level, name, hp, mp)
        self.tp_rate = tp_rate

    def attack(self):
        print(f"{self.name}必殺技で攻撃する。")

    def encourage(self):
        print(f"{self.name}がみんなを勇気づける。")

    def calc_tp(self):
        return (self.hp + self.mp) * self.tp_rate


print("===Player object===")
john = Player(1, "John", 20, 0)
john.attack()
john.show()
# john.encourage()

print("\n===Hero object===")
leo = Hero(30, "Leo", 300, 150, 2)
leo.attack()
leo.show()
leo.encourage()
print(f"tp of {leo.name}: {leo.calc_tp()}")
