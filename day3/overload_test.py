class overload():
    def showkey(self, x : int, letter : str):
        b = x + 2
        return letter + str(b)

    def showkey(self, x : int, letter : str):
        a = 123 + x
        return letter + str(a)


A = overload()
B = A.showkey(3, "A")
print(B)
