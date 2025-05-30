class Fish:
    def __init__(self, color):
        self.color = color

    def swim(self):
        print("泳ぐ")

    def sleep(self):
        print("寝る")


f1 = Fish("blue")
print(f"fish color {f1.color}")
f1.swim()
f1.sleep()
