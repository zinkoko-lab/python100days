# コンポジションに関する例のコードです。
class Engine:

    def start(self):
        print("エンジンを始動します")

    def stop(self):
        print("エンジンを停止します")


class Car:

    def __init__(self, brand):
        self.brand = brand
        self.engine = Engine()

    def start(self):
        print(f"{self.brand}の車をスタートさせます")
        self.engine.start()

    def stop(self):
        print(f"{self.brand}の車を停止させます")
        self.engine.stop()


my_car = Car("Toyota")
my_car.start()
my_car.stop()
