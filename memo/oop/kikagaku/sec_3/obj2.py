class Player:
    def __init__(self, level, name):
        self.__level = level
        self.__name = name

    def set_level(self, level):
        if isinstance(level, int):
            self.__level = level

    def get_level(self):
        return self.__level

    def set_name(self, name):
        if isinstance(name, str) and name != "":
            self.__name = name

    def get_name(self):
        return self.__name

    def attack(self):
        print(f"{self.__name}が攻撃する。")


john = Player(1, "JOHN")
john.attack()
print(f"get_name: {john.get_name()}")
print(f"get_level: {john.get_level()}")

print("\n==============setter適用後==============")
john.set_level(5)
john.set_name("New_JOHN")
john.attack()
print(f"get_name: {john.get_name()}")
print(f"get_level: {john.get_level()}")
