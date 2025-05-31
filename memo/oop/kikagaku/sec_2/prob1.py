class Dog:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"私は{self.name}です。")


class SuperDog(Dog):

    def speak(self):
        print("人間の言葉を話します。")


print("===dog object===")
dg = Dog("リリ")
print(f"{dg} <- dog objectのメモリ上のアドレス")
dg.show()

print("\n===Super dog object===")
sd = SuperDog("ゆゆ")
print(f"{sd} <- super dog objectのメモリ上のアドレス")
sd.show()
sd.speak()
