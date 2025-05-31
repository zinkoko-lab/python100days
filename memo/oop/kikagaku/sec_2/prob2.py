class Rectangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def show(self):
        print(f"底辺{self.base}、高さ{self.height}の長方形です。")

    def calc_area(self):
        return self.base * self.height


class RectangleEx(Rectangle):

    def calc_circumference(self):
        return (self.base + self.height) * 2


print("===Rectangle Object===")
rtg = Rectangle(30, 50)
print(f"{rtg} <- memory address")
rtg.show()
print(f"Area: {rtg.calc_area()}")

print("\n===RectangleEx Object===")
rtg_ex = RectangleEx(70, 80)
print(f"{rtg_ex} <- memory address")
rtg_ex.show()
print(f"Area: {rtg_ex.calc_area()}")
print(f"Circumference: {rtg_ex.calc_circumference()}")
