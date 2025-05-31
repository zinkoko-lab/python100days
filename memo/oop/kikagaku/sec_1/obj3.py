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

    def salary_up(self, salary_up_amount):
        self.salary += salary_up_amount
        # return self.salary

    def br_update(self, new_br):
        self.bonus_rate = new_br
        # return new_br


hiro = Worker(1, "HIRO", 25, 200000)
print(hiro)ß
hiro.show()
hiro.work()
print(f"salary : {hiro.calc_salary()}")
print(f"bonus : {hiro.calc_bonus()}")

hiro.salary_up(20000)
hiro.br_update(3)

print(hiro)
hiro.show()
hiro.work()
print(f"salary : {hiro.calc_salary()}")
print(f"bonus : {hiro.calc_bonus()}")
