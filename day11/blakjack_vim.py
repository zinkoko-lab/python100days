import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

while True:
    play = input("Do you want to play a game of Blackjack? Type y or n: ")

    if play != 'y':
        break
    else:
        # hand out each two cards for each(player & computetr)
        hands = {"player":[], "computer":[]}
        for _ in range(2):
            hands["player"].append(random.choice(cards))
            hands["computer"].append(random.choice(cards))

        # write a function to calculate the score

        # ACE 1 card:
        # if hands have one ACE card and sum of another cards < 11 : ace = 11
        # if hands have one ACE card and sum of another cards => 11 : ace = 1

        # ACE 2 cards:
        # if hands have two cards and sum of another cards < 10 : ace = 11, ace = 1
        # if hands have two cards and sum of another cards >= 10 : ace = 1, 1

        # ACE N cards and more:
        # if hands h

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

        # else(user stopped hit and user score < 21)

        # If user stopped hitting the cards, computer start hit the cards under the specific rules.
        # Rules for computer:
        # If computer_score <= 16: hit the cards
        # If computer_score >= 17: stand

        # If computer_score > player_score:
        #   computer win
        # If computer_score < player_score:
        #   user win
        # else: draw
