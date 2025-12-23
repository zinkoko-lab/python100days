# Level-6: Polymorphism
"""
ポリモーフィズム（Polymorphism）とは、オブジェクト指向プログラミングにおける「多様性」「多態性」を意味し、同じ名前のメソッド（命令）が、オブジェクトの種類（クラス）によって異なる振る舞いをすることです。これにより、異なるクラスのオブジェクトを**共通のインターフェース（窓口）**を通して扱え、コードの再利用性や拡張性、柔軟性が向上します。例えば、同じ`draw()`メソッドでも、Circleオブジェクトなら円を描き、Squareオブジェクトなら四角形を描く、といった実現を可能にします
"""


class Animal:
    def speak(self):
        return "..."


class Dog(Animal):
    def speak(self):  # オーバーライド
        return "Wan!"


class Cat(Animal):
    def speak(self):  # オーバーライド
        return "Nyaa~"


# 異なるオブジェクトが同じspeakメソッドを持つ
animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.speak())  # Wan!, Nyaa~, ... と出力される
