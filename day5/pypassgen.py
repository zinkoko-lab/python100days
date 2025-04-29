import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '@', '+', '*']

print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password?\n"))
num_nums = int(input("How many numbers would you like?\n"))
num_symbols = int(input("How many symbols would you like?\n"))

list_for_passgen = []

for _ in range(num_letters):
    list_for_passgen.append(random.choice(letters))

for _ in range(num_nums):
    list_for_passgen.append(random.choice(numbers))

for _ in range(num_symbols):
    list_for_passgen.append(random.choice(symbols))

random.shuffle(list_for_passgen)

password = ""
for idx in range(len(list_for_passgen)):
    password += list_for_passgen[idx]

print(password)