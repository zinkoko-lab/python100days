class Dog:
    def __init__(self, name='名無し'):
        self.name = name

    def show(self):
        print('私は{}です。'.format(self.name))

class Superdog(Dog):
    def speak(self):
        print('{}は人間の言葉を話します。'.format(self.name))

    def show(self):
        print('私は魔法が使える犬 {}です。'.format(self.name))

d = Dog()
d.show()

s = Superdog()
s.show()
