# Level-2: Class Variables and Instance Variables
# Using class and Instance variables


class Student:
    school = "ABC school"  # Class variable

    def __init__(self, name):
        self.name = name  # Instance variable


s1 = Student("Alice")
s2 = Student("Bob")

print(s1.name)
print(s2.school)
