import random
cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def hand_out(card_list: list):
    for _ in range(2):
        card_list.append(random.choice(cards))

player_cards = []
computer_cards = []

hand_out(player_cards)
hand_out(computer_cards)

player_score = sum(player_cards)

while player_score < 21:
    print(f"\tYour cards: {player_cards}, current score: {player_score}")
    print(f"\tComputer's first card: {computer_cards[0]}")
    draw = input("Type 'y' to get another card, type 'n' to pass: ")
    if draw != 'y':
        break
    else:
        player_cards.append(random.choice(cards))
        player_score = sum(player_cards)

computer_score = sum(computer_cards)

if computer_score <= 16:
    while computer_score < 21:
        computer_cards.append(random.choice(cards))
