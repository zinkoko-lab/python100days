# コンポジションに関する例のコードです。
class Person:

    def __init__(self, name):
        self.name = name

    def hello(self):
        print("おはようございます")


class Bird:

    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

    def hello(self):
        self.owner.hello()


takashi = Person("たかし")
pchan = Bird("ぴーちゃん", takashi)

print(pchan.owner.name)
pchan.hello()
