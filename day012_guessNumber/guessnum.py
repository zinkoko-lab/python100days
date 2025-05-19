from random import randint
import logo
import os

# Global variables
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def generate_number():
    """Generate a random number from 1 to 100"""
    return randint(1, 100)

def greeting():
    """Print the greeting text of the game."""
    greeting_text = r'''
    Welcome to the Number Guessing Game!
    I'm thinking of a number between 1 and 100.
    '''
    print(greeting_text)

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def choose_level(level: str):
    """Return the number of attempts based on difficulty level."""
    if level in ['easy', 'hard']:
        if level == 'easy':
            return EASY_LEVEL_TURNS
        else:
            return HARD_LEVEL_TURNS
    return False

def guess_a_number():
    """Prompt the user to input a number. Return the number or False on invalid input."""
    try:
        guessed_num = int(input("Make a guess: "))
        if guessed_num > 0:
            return guessed_num
    except:
        return False

def get_a_hint(guessed_number: int, actual_number: int):
    """Give feedback on the guessed number compared to the correct answer."""
    if guessed_number > actual_number:
        print("Too high.")
        return False
    elif guessed_number < actual_number:
        print("Too low.")
        return False
    else:
        print(f"You got it! The answer was {actual_number}\n")
        return True

def decrease_life(cur_life: int):
    """Decrease remaining attempts and display the count."""
    cur_life -= 1
    if cur_life > 0:
        print(f"You have {cur_life} attempts remaining to guess the number.\n")
    else:
        print("You've run out of guesses. Restart the game.")
    return cur_life

def play_the_game():
    """Main function to play the game."""
    rdn_number = generate_number()
    level_input = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    life = choose_level(level_input)
    if life:
        while life > 0:
            input_number = guess_a_number()
            if input_number:
                result = get_a_hint(input_number, rdn_number)
                if result:
                    return
                else:
                    if life > 1:
                        print("Guess again.")
                    life = decrease_life(life)
            else:
                print("You typed wrong input. Restart the game.\n")
                return
        if life == 0:
            print(logo.game_over + '\n')
            return
    else:
        print("You typed wrong input. Restart the game.\n")
        return

# -------------------------------
# Main Game Loop
# -------------------------------
while input("Do you want to play the game \"GUESS THE NUMBER\".\nType 'y' or 'n': ").lower() == 'y':
    clear_screen()
    print(logo.game_logo)
    greeting()
    play_the_game()

clear_screen()
