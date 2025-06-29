import pandas as pd
from os import system, name, path


def clear_screen():
    system("cls" if name == "nt" else "clear")


try:
    df = pd.read_csv("nato_phonetic_alphabet.csv")
except FileNotFoundError:
    print("nato_phonetic_alphabet.csv file not found.")
    exit(1)

nato_phonetic_dict = {row.letter.upper(): row.code for _, row in df.iterrows()}


def generate_nato_words():
    input_word = input("Enter a word: ").upper()
    try:
        result = [nato_phonetic_dict[letter] for letter in input_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_nato_words()
    else:
        print(result)


while True:
    clear_screen()
    print("NATO Phonetic Alphabet Project")
    try:
        generate_nato_words()
        do_continue = input("Do you have any other words(y/n): ").lower()
        if do_continue != "y":
            break
    except KeyboardInterrupt:
        print("\nExiting.")
        break

clear_screen()
