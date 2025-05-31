class Rectangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def show(self):
        print(f"底辺{self.base}、高さ{self.height}の長方形です。")

    def calc_area(self):
        return self.base * self.height


r = Rectangle(1000, 500)
r.show()
print(f"Area: {r.calc_area()}")
