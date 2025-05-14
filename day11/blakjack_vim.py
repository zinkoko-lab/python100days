import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

while True:
    play = input("Do you want to play a game of Blackjack? Type y or n: ")

    if play != 'y':
        break
    else:
        # hand out each two cards for each(player & computetr)
        # show all the player's cards and score
        # show the first card of computer.

        # If one or both has score of 21, it possible 3 cases.
        # 1.user win with blackjack.
        # 2.computer win with blackjack.
        # 3.both have blackjack and draw.

        # If non of above:

        # Ask user to hit extra card or not, while user score < 21.

        # during hitting of user, user score > 21

        # user lose.

        # if user score = 21(not natural blackjack)
        #   if user score > computer score:
        #       user win with blackjack
        #   if user score = computer score:
        #       draw

        # else(user stopped hit and user score < 21)

        # If user stopped hitting the cards, computer start hit the cards under the specific rules.
        # Rules for computer:
        # If computer_score <= 16: hit the cards
        # If computer_score >= 17: stand

        # 
