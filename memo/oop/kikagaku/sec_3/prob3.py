# ==========================================
# Player クラスと Hero クラスのサンプル
# - Playerクラス：プレイヤーの基本的な動作
# - Heroクラス：Playerを継承し、必殺技などの追加機能を持たせる
# ==========================================


class Player:
    # クラス変数：プレイヤーのレベル上限
    LEVEL_LIMIT = 50

    def __init__(self, level, name, hp, mp):
        # レベルが上限を超えないようにチェック
        if level > Player.LEVEL_LIMIT:
            self.level = Player.LEVEL_LIMIT
        else:
            self.level = level
        # インスタンス変数：名前、HP、MP
        self.name = name
        self.hp = hp
        self.mp = mp

    def attack(self):
        # プレイヤーの攻撃動作
        print(f"{self.name}が敵を攻撃する。")

    def show(self):
        # プレイヤー情報を表示
        print(f"level: {self.level}\nname: {self.name}\nhp: {self.hp}\nmp: {self.mp}")

    def check_level(self):
        # レベルが上限を超えた場合は上限に修正する
        if self.level > Player.LEVEL_LIMIT:
            self.level = Player.LEVEL_LIMIT

    def level_up(self, up):
        # レベルアップ処理
        self.level += up
        self.check_level()


class Hero(Player):
    def __init__(self, level, name, hp, mp, tp_rate):
        # Playerクラスのコンストラクタを呼び出して初期化（super()を使う）
        super().__init__(level, name=name, hp=hp, mp=mp)
        # Hero専用のインスタンス変数：TP（必殺技ゲージのたまり具合）
        self.tp_rate = tp_rate

    def attack(self):
        # Heroクラスでattackメソッドをオーバーライド（必殺技）
        print(f"{self.name}が必殺技で攻撃する。")

    def encourage(self):
        # Heroクラス専用メソッド
        print(f"{self.name}がみんなを勇気づける。")


# ==========================================
# 動作確認
# ==========================================

print("===Player object===")
john = Player(1, "John", 20, 0)  # Playerオブジェクト生成
john.attack()  # Johnが敵を攻撃する。
john.show()  # Johnのステータス表示

print("===John level up by 20===")
john.level_up(20)  # Johnのレベルを20上げる
john.show()  # 上限に収まっていればそのまま表示


print("\n===Hero object===")
leo = Hero(30, "Leo", 300, 150, 2)  # Heroオブジェクト生成
leo.attack()  # Leoが必殺技で攻撃する。
leo.show()  # Leoのステータス表示
leo.encourage()  # Leoがみんなを勇気づける。

print("===Leo level up by 50===")
leo.level_up(50)  # 上限(50)を超えるようにレベルアップ
leo.show()  # 上限(50)で表示される


print("\n===Hero object===")
# 最初からlevelを60（上限オーバー）でHeroを生成
rei = Hero(60, "Rei", 300, 150, 2)
rei.attack()  # Reiが必殺技で攻撃する。
rei.show()  # レベルは50として表示される（上限適用）
rei.encourage()  # Reiがみんなを勇気づける。
