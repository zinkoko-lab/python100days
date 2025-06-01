# ==========================================
# このコードは、DogクラスとSuperDogクラスを定義し、
# クラス変数のカプセル化、名前修飾、継承、メソッドオーバーライドを学ぶためのサンプルです。
# ==========================================


class Dog:
    # クラス変数（カプセル化）→ __species は直接アクセスできない（名前修飾される）
    __species = "イヌ"

    def __init__(self, name="名無し"):
        # インスタンス変数（カプセル化）→ __name は直接アクセスできない（名前修飾される）
        self.__name = name

    # クラス変数 __species を外部（サブクラス含む）からアクセスできるようにgetterメソッドを作成
    def get_species(self):
        return Dog.__species

    # インスタンスの名前を表示
    def show(self):
        print(f"私は{Dog.__species} {self.__name}です。")

    # インスタンス変数 __name のgetterメソッド
    def get_name(self):
        return self.__name

    # インスタンス変数 __name のsetterメソッド（安全に名前を変更）
    def set_name(self, other_name):
        if isinstance(other_name, str) and other_name != "":
            self.__name = other_name


class SuperDog(Dog):
    # showメソッドをオーバーライド（スーパークラスのshowを拡張）
    def show(self):
        # get_species() 経由でクラス変数 __species にアクセス
        # get_name() 経由でインスタンス変数 __name にアクセス
        print(f"私は魔法が使える{self.get_species()} {self.get_name()}です。")

    # SuperDog 独自のメソッド
    def speak(self):
        print(f"{self.get_species()} {self.get_name()}は人間の言葉を話します。")

    # もし直接Dog.__speciesにアクセスしようとするとエラーになる例（コメントアウト）
    # def show_species(self):
    #     print(Dog.__species)  # ← これはエラーになる！
    #     # AttributeError: type object 'Dog' has no attribute '__species'


# ==========================================
# 動作確認
# ==========================================

print("===== Dog object =====")
dog1 = Dog()  # 名前が「名無し」のDogオブジェクトを生成
dog1.show()  # 私は名無しです。
dog1.set_name("リリ")  # 名前を「リリ」に設定
print("===== name 設定後 =====")
dog1.show()  # 私はリリです。

print("\n===Super dog object===")
dog2 = SuperDog()  # 名前が「名無し」のSuperDogオブジェクトを生成
dog2.show()  # 私は魔法が使えるイヌ 名無しです。
dog2.speak()  # 名無しは人間の言葉を話します。

dog2.set_name("ゆゆ")  # 名前を「ゆゆ」に設定
print("===== name 設定後 =====")
dog2.show()  # 私は魔法が使えるイヌ ゆゆです。
dog2.speak()  # ゆゆは人間の言葉を話します。
