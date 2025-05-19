print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?: "))

if height >= 120:
    print("You can ride the rollercoaster.")
    bill = 0
    age = int(input("What is your age?: "))
    midAge = 45 <= age <= 55
    if not midAge:
        if age < 12:
            print("Child tickets are $5.")
            bill += 5
        elif age <= 18:
            print("Youth tickets are $7.")
            bill += 7
        else:
            print("Adult tickets are $12.")
            bill += 12

    else:
        print("Everything is going to be ok. Have a free ride on us!")

    want_photo = input("Do you want to have a photo take? Type y for Yes or n for No. ")
    if want_photo == "y":
        bill += 3

        print(f"Your final bill is ${bill}.")

else:
    print("Sorry you have to grow taller before you can ride")



# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm?: "))

# if height >= 120:
#     print("You can ride the rollercoaster.")
# else:
#     print("Sorry you have to grow taller before you can ride")

# number = int(input("Enter an integer: "))
# remainder = number % 2
# if remainder == 0:
#     print("The integer is even.")
# else:
#     print("The integer is odd")
