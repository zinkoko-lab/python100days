class Dog:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"私は{self.name}です。")


hachi = Dog("ハチ")
hachi.show()
