# ポリモーフィズム（多態性）についての例のコードです


# 基本のPlayerクラスを定義します。
# これは「プレイヤー」という共通の性質を表します。
class Player:
    # コンストラクタ（初期化メソッド）
    def __init__(self, name):
        self.name = name  # プレイヤーの名前をインスタンス変数に格納

    # attackメソッド：プレイヤーが攻撃する
    def attack(self):
        print(f"{self.name}は攻撃する。")


# HeroクラスはPlayerクラスを継承します。
# Playerクラスの機能を引き継ぎ、attackメソッドをオーバーライド（上書き）しています。
class Hero(Player):
    def attack(self):
        print(f"{self.name}は剣で攻撃する。")


# MageクラスもPlayerクラスを継承します。
# attackメソッドをオーバーライドしています。
class Mage(Player):
    def attack(self):
        print(f"{self.name}は魔法で攻撃する。")


# PersonクラスはPlayerクラスと継承関係がありません。
# しかし、同じ名前のattackメソッドを持っているため、
# ポリモーフィズムの例として利用できます。
class Person:
    def attack(self):
        print("様子を見る。")


# ここまでで、すべてのクラスに同じ名前のメソッド attack() が定義されていることがわかります。

# それぞれのクラスのオブジェクト（インスタンス）を作成し、
# playersというリストにまとめます。
players = []
players.append(Player("JOHN"))  # 基本のプレイヤー
players.append(Hero("LEO"))  # ヒーロー
players.append(Mage("REI"))  # 魔法使い
players.append(Person())  # 人（名前なし）

# playersリストの中のすべてのオブジェクトに対して
# 同じメッセージ（attackメソッド）を送ります。
# 継承関係にあるPlayerのサブクラスも、継承関係のないPersonクラスも
# それぞれのattackメソッドが呼ばれます。
# これがポリモーフィズム（同じメッセージでもオブジェクトごとに動きが異なる）です。
for player in players:
    player.attack()
