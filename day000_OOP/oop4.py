# level-4: Method Overriding

# Overriding a method in the child class


# parent class
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def math(self, score):
        print(score)


# child class
class Grade1(Student):
    # overriding __init__ method of the Student class
    def __init__(self, name, age):
        super().__init__(name, age)
        print("Name :", self.name)
        print(" Age :", self.age)

    # overriding math method of the Student class
    def math(self, score):
        print(f"math: {score}")

    def english(self, score):
        print(f"english: {score}")


studentA = Student("Yamada", 15)
studentB = Grade1("Sato", 12)
studentA.math(78)
studentB.math(78)
studentB.english(80)
