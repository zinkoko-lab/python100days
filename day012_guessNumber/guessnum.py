import random
import logo
import os

# Generate a random number from 1 to 100
rdn_num = random.randrange(1, 101)

greeting = r'''
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
'''

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def choose_level(level: str):
    """Return the number of attempts based on difficulty level."""
    if level in ['easy', 'hard']:
        return 10 if level == 'easy' else 5
    return False

def guess_a_number():
    """Prompt the user to input a number. Return the number or False on invalid input."""
    try:
        guessed_num = int(input("Make a guess: "))
        if guessed_num > 0:
            return guessed_num
    except:
        return False

def get_a_hint(number: int):
    """Give feedback on the guessed number compared to the correct answer."""
    if number > rdn_num:
        print("Too high.")
        return False
    elif number < rdn_num:
        print("Too low.")
        return False
    else:
        print(f"You got it! The answer was {rdn_num}\n")
        return True

def decrease_life(cur_life: int):
    """Decrease remaining attempts and display the count."""
    cur_life -= 1
    if cur_life > 0:
        print(f"You have {cur_life} attempts remaining to guess the number.\n")
    else:
        print("You've run out of guesses. Restart the game.")
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
                    if life > 1:
                        print("Guess again.")
                    life = decrease_life(life)
            else:
                print("You typed wrong input. Restart the game.\n")
                break
        if life == 0:
            print(logo.game_over + '\n')
    else:
        print("You typed wrong input. Restart the game.\n")

clear_screen()
