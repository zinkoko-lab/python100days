class Dog:

    def __init__(self, name="名無し"):
        self.name = name

    def show(self):
        print(f"私は{self.name}です。")


class SuperDog(Dog):

    def show(self):
        print(f"私は魔法が使える犬{self.name}です。")

    def speak(self):
        print(f"{self.name}は人間の言葉を話します。")


print("===== Dog object =====")
dog1 = Dog()
dog1.show()

print("\n===Super dog object===")
dog2 = SuperDog()
dog2.show()
dog2.speak()
