class Worker:

    __bonus_rate = 2  # クラス変数です
    __num = 0  # 社員数の初期値を0とし、クラス変数及びカプセル化して定義する

    def __init__(self, id, name, age, salary):
        self.id = id
        self.name = name
        self.age = age
        self.salary = salary
        Worker.__num += 1

    def show(self):
        print(f"id: {self.id}\nname: {self.name}\nage: {self.age}")

    def work(self):
        print(f"{self.name}さんが働く。")

    def calc_salary(self):
        return self.salary

    def calc_bonus(self):
        return self.salary * Worker.__bonus_rate

    # 社員数を参照するクラスメソッドをgetterメソッドとして定義する
    @classmethod
    def get_num(cls):
        return cls.__num

    # bonus_rateを参照するクラスメソッドをgetterメソッドとして定義する
    @classmethod
    def get_bonus_rate(cls):
        return cls.__bonus_rate

    # 会社の規定変更等によりbonus_rateの変更が想定される
    # そのためbonus_rateを再設定するsetterメソッドをクラスメソッドとして定義しておく
    @classmethod
    def set_bonus_rate(cls, new_bonus_rate):
        cls.__bonus_rate = new_bonus_rate


print(f"Work classのBONUS_RATE = {Worker.get_bonus_rate()}")
print(f"社員数: {Worker.get_num()}")

print("=== HIRO のオブジェクトの生成 ===")
hro = Worker(1, "HIRO", 25, 200000)
hro.show()
print(f"{hro.name}さんの月給: {hro.calc_salary()}")
print(f"{hro.name}さんの賞与: {hro.calc_bonus()}")
print(f"社員数: {Worker.get_num()}")

print("=== YUKI のオブジェクトの生成 ===")
yki = Worker(300, "YUKI", 35, 400000)
yki.show()
print(f"{yki.name}さんの月給: {yki.calc_salary()}")
print(f"{yki.name}さんの賞与: {yki.calc_bonus()}")
print(f"社員数: {Worker.get_num()}")

print("=== bonus_rateの変更 ===")
Worker.set_bonus_rate(3)
print(f"Work classのBONUS_RATE = {Worker.get_bonus_rate()}")
