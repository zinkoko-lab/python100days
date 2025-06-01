import module2


class ClassB(module2.ClassA):
    def new_method(self):
        print("module test: new_method")


module2.func()
b = ClassB("testB")
print(b.name)
b.method()
b.new_method()
