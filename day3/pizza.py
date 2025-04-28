print("Welcome to Python Pizza Deliveries!")

bill = 0
flag = False
while not flag:
    size = input("What size of pizza do you want? S, M, or L: ")
    if size == "S":
        bill += 15
        flag = True
    elif size == "M":
        bill += 20
        flag = True
    elif size == "L":
        bill += 25
        flag = True
    else:
        print("You typed wrong input. Please input S, M, or L")
        flag = False

flag = False
while not flag:
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    if pepperoni == "Y":
        if size == "S":
            bill +=2
            flag = True
        else:
            bill += 3
            flag = True
    elif pepperoni == "N":
        flag = True
    else:
        print("You typed wrong input. Please input Y or N")
        flag = False

flag = False
while not flag:
    extra_cheese = input("Do you want extra cheese? Y or N: ")
    if extra_cheese == "Y":
        bill += 1
        flag = True
    elif extra_cheese == "N":
        flag = True
    else:
        print("You typed wrong input. Please input Y or N")
        flag = False

print(f"Your final bill is ${bill}")
