import pandas as pd
from os import system, name


def clear_screen():
    system("cls" if name == "nt" else "clear")


try:
    df = pd.read_csv("nato_phonetic_alphabet.csv")
except FileNotFoundError:
    print("nato_phonetic_alphabet.csv file not found.")
    exit(1)

nato_phonetic_dict = {row.letter.upper(): row.code for _, row in df.iterrows()}


def generate_nato_words():
    print("Credit to NORTH ATLANTIC TREATY ORGANIZATION")
    input_word = input("Enter a word: ").upper()
    result = []
    for letter in input_word:
        code = nato_phonetic_dict.get(letter)
        if code:
            result.append(code)
        else:
            print(f"Warning: '{letter}' is not a valid letter.")
    print(result)


while True:
    clear_screen()
    try:
        generate_nato_words()
        do_continue = input("Do you have any other words(y/n): ").lower()
        if do_continue != "y":
            break
    except KeyboardInterrupt:
        print("\nExiting.")
        break

clear_screen()
