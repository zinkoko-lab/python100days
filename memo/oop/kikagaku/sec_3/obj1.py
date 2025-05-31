# このソースコードはデフォルト引数の機能を実装する例です
class Player:
    def __init__(
        self, level=1, name="???", hp=10, mp=0
    ):  # level, name, hp, mp　等のデフォルト値として定義
        self.level = level
        self.name = name
        self.hp = hp
        self.mp = mp

    def attack(self, air="普通に"):
        print(f"{self.name}が敵を{air}攻撃する。")

    def show(self):
        print(f"level: {self.level}\nname: {self.name}\nhp: {self.hp}\nmp: {self.mp}")


class Hero(Player):
    def encourage(self):
        print("みんなを勇気づける。")


p = Player()
john = Player(1, "JOHN", 20, 0)
leo = Hero(30, "LEO", 300, 150)

# インスタンス変数に何も指定しないと、値がデフォルト引数で指定されている値となる
print("インスタンス変数に何も指定しないと、値がデフォルト引数で指定されている値となる↓")
p.show()
p.attack()

print("\nインスタン変数に値を指定した時のオブジェクト")
john.show()
john.attack("懸命に")

print("\nsubclass Heroの場合 ->")
leo.show()
leo.attack("全力で")
