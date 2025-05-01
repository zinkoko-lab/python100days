#!/usr/bin/env python3
import random
print(r'''
What do you choose? 
Type 0 for Rock, 1 for Paper or 2 for Scissors.
''')

rock = r'''
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        '''

paper = r'''
            _______
        ---'   ____)____
                  ______)
                  _______)
                 _______)
        ---.__________)
        '''

scissors = r'''
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        '''

def hand_signal(num):
    if num == 0:
        print(rock)
    elif num == 1:
        print(paper)
    elif num == 2:
        print(scissors)
    else:
        return

humanChoice = int(input(""))
if (humanChoice == 0) or (humanChoice == 1) or (humanChoice == 2):
    print("You chose:")
    hand_signal(humanChoice)
    computerChoice = random.randint(0, 2)
    print("Computer chose:")
    hand_signal(computerChoice)

    if humanChoice == computerChoice:
        print("It's a draw.")
    elif humanChoice == 0:
        if computerChoice == 2:
            print("You win.")
        else:
            print("You lose.")
    elif humanChoice == 1:
        if computerChoice == 0:
            print("You win.")
        else:
            print("You lose.")
    else:
        if computerChoice == 1:
            print("You win.")
        else:
            print("You lose.")
else:
    print("You typed an invalid number, you lose!")