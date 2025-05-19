import random
import logo
import os

# Generate a number randomly from 1 to 100
rdn_num = random.randrange(1, 101)

greeting = r'''
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
'''
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def choose_level(level: str):
    if level in ['easy', 'hard']:
        if level == 'easy':
            return 10
        else:
            return 5
    else:
        return False

# Request user to guess the number
def guess_a_number():
    try:
        guessed_num = int(input("Make a guess:"))
        if guessed_num > 0:
            return guessed_num
    except:
        # 数字以外が入力された場合
        return False

def get_a_hint(number: int):
    if number > rdn_num:
        print("Too high.\nGuess again.")
        return False
    elif number < rdn_num:
        print("Too low.\nGuess again.")
        return False
    else:
        print(f"You got it! The answer was {rdn_num}")
        print("\n")
        return True

def decrease_life(cur_life: int):
    cur_life -= 1
    print(f"You have {cur_life} attempts remaining to guess the number.")
    print("\n")
    return cur_life

while input("Do you want to play the game \"GUESS THE NUMBER\".\nType 'y' or 'n': ").lower() == 'y':
    clear_screen()
    print(logo.game_logo)
    print(greeting)

    level_input = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    life = choose_level(level_input)

    if life:
        while life > 0:
            a_number = guess_a_number()
            if a_number:
                result = get_a_hint(a_number)
                if result:
                    break
                else:
                    life = decrease_life(life)
            else:
                print("You typed wrong input. Force quit from the game.")
                break
        if life == 0:
            print(logo.game_over)
            print('\n')
            continue
        else:
            continue
    else:
        print("You typed wrong input. Force quit from the game.")
        continue

clear_screen()
