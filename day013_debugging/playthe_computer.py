# year = int(input("What's your year of birth?"))

# # year = 1994

# # (1994 > 1980)True and (1994 < 1994)False = False
# if year > 1980 and year < 1994:
#     print("You are a millennial.")
# # 1994 > 1994 = False
# elif year > 1994:
#     print("You are a Gen Z.")
while True:
    try:
        age = int(input("How old are you?: "))
        break
    except ValueError:
        print("Your input is not valid. Please try again with a numerical input like 15.")


if age >= 18:
    print(f"You can drive at age {age}.")
else:
    print(f"You can't drive at age {age}.")
