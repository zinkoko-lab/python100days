class Circle:

    PI = 3.1215  # これはクラス変数です

    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        return self.radius**2 * Circle.PI

    @classmethod
    def radians(cls, degree):
        return degree * (
            cls.PI / 180
        )  # classmethod の中でクラス変数を使いたい時は cls. をつける


c = Circle(float(input("円の半径をmm単位入力してください: ")))
print(f"半径{c.radius} mmの円です。")
print(f"PI = {Circle.PI}")  # 直接クラス変数を呼び出すことができる
print(f"円の面積は {c.calc_area()} mm^2 です。")

deg = float(input("角度をdegree単位で入力してください: "))
rad = Circle.radians(deg)
print(f"{deg} degree = {rad} radian")
