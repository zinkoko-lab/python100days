def func():
    print("module test: func")

class ClassA:
    def __init__(self, name):
        self.name = name

    def method(self):
        print("module test: method")

if __name__ == "__main__":
    func()
    obj = ClassA("test")
    obj.method()