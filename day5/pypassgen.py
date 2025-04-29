import random
from random import shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '@', '+', '*']

print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password?\n"))
num_nums = int(input("How many numbers would you like?\n"))
num_symbols = int(input("How many symbols would you like?\n"))

len_letters = len(letters)
len_numbers = len(numbers)
len_symbols = len(symbols)

list_for_passgen = []

for cnt in range(num_letters):
    idx = random.randint(0, len_letters-1)
    list_for_passgen.append(letters[idx])

for cnt in range(num_nums):
    idx = random.randint(0, len_numbers-1)
    list_for_passgen.append(numbers[idx])

for cnt in range(num_symbols):
    idx = random.randint(0, len_symbols-1)
    list_for_passgen.append(symbols[idx])

random.shuffle(list_for_passgen)

password = ""
for idx in range(len(list_for_passgen)):
    password += list_for_passgen[idx]

print(password)