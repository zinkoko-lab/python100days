class Worker:

    def __init__(self, id, name, age, salary):
        self.id = id
        self.name = name
        self.age = age
        self.salary = salary
        self.bonus_rate = 2

    def show(self):
        print(f"id : {self.id}\nname : {self.name}\nage : {self.age}")

    def work(self):
        print(f"{self.name}さんが働く。")

    def calc_salary(self):
        return self.salary

    def calc_bonus(self):
        return self.salary * self.bonus_rate


class Manager(Worker):

    def __init__(self, id, name, age, salary, allowance):
        super().__init__(id=id, name=name, age=age, salary=salary)
        self.allowance = allowance

    def budget_manage(self):
        print(f"{self.name}さんが予算管理をする。")

    def work(self):
        print("進捗管理をする。")

    def calc_salary(self):
        return self.salary + self.allowance


mng = Manager(300, "YUKI", 35, 400000, 50000)
mng.show()
mng.work()
mng.budget_manage()
print(f"{mng.name}さんの月給: {mng.calc_salary()}")
print(f"{mng.name}さんの賞与: {mng.calc_bonus()}")
print(f"{mng.name}さんの月給の内訳:")
print(f"基本給: {mng.salary}")
print(f"マネージャー手当: {mng.allowance}")
