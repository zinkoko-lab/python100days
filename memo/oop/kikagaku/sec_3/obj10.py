# ポリモーフィズムのハンズオンのコードです
class Worker:

    def __init__(self, name):
        self.name = name

    def work(self):
        print(f"{self.name}は働く。")


class Sales(Worker):

    def work(self):
        print(f"{self.name}は客先に行く。")


class Engineer(Worker):

    def work(self):
        print(f"{self.name}はプログラムを作成する。")


class Partner:

    def work(self):
        print("仕事をする。")


workers = []
workers.append(Worker("田中さん"))
workers.append(Sales("高橋さん"))
workers.append(Engineer("大林さん"))
workers.append(Partner())

for worker in workers:
    worker.work()
