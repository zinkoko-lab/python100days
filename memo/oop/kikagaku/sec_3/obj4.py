class Worker:

    bonus_rate = 2  # クラス変数です

    def __init__(self, id, name, age, salary):
        self.id = id
        self.name = name
        self.age = age
        self.salary = salary

    def show(self):
        print(f"id: {self.id}\nname: {self.name}\nage: {self.age}")

    def work(self):
        print(f"{self.name}さんが働く。")

    def calc_salary(self):
        return self.salary

    def calc_bonus(self):
        return self.salary * Worker.bonus_rate


hro = Worker(1, "HIRO", 25, 200000)
hro.show()
print(f"{hro.name}さんの月給: {hro.calc_salary()}")
print(f"Work classのBONUS_RATE = {Worker.bonus_rate}")
print(f"{hro.name}さんの賞与: {hro.calc_bonus()}")
