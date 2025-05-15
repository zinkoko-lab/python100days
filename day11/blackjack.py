import random
import os
from logo import art

# ターミナルの画面をクリアする関数を定義
# os.name が 'nt' の場合は Windows ⇒ 'cls' コマンド
# それ以外（macOS / Linux）の場合は 'clear' コマンドを使用
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# constants
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
init_handout = 2    # initial handout is two cards for each
ace = 11            # original ace
alt_ace = 1         # alternative ace
magic_number = 12   # magic number from my logical thinking
black_jack = 21     # ultimate score
computer_lmt = 17   # after user's hit, computer consider hit or not base upon this limit score

# procedure to hand out each two cards for each
def hand_out():
    for _ in range(init_handout):
        hands["player"]["cards"].append(random.choice(deck))
        hands["computer"]["cards"].append(random.choice(deck))

# function to calculate score
def calc_score(cards: list):
    dummy_lst = []
    if ace in cards:
        ace_cnt = cards.count(ace)
        score_lmt = magic_number - ace_cnt
        score_without_ace = sum([_ for _ in cards if _ != ace])
        if score_without_ace >= score_lmt:
            for card in cards:
                if card == ace:
                    dummy_lst.append(alt_ace)
                else:
                    dummy_lst.append(card)
        else:
            first_ace_idx = cards.index(ace)
            for idx in range(len(cards)):
                if idx != first_ace_idx:
                    if cards[idx] == ace:
                        dummy_lst.append(alt_ace)
                    else:
                        dummy_lst.append(cards[idx])
                else:
                    dummy_lst.append(cards[idx])
    else:
        dummy_lst = cards

    return sum(dummy_lst)

# calculate the scores of both
def save_scores():
    hands["player"]["score"] = calc_score(hands["player"]["cards"])
    hands["computer"]["score"] = calc_score(hands["computer"]["cards"])

# procedure of to hit
def hit(who: str):
    players = list(hands.keys())
    if who in players:
        hands[who]["cards"].append(random.choice(deck))
        hands[who]["score"] = calc_score(hands[who]["cards"])

# procedure to show all the player's cards and score
# and show the first card of computer
def show():
        print(f"\tYour cards: {hands["player"]["cards"]}, current score: {hands['player']["score"]}")
        print(f"\tComputer's first card: {hands['computer']["cards"][0]}")

# procedure to declare final condition
def decl_fnl_cond():
    print(f"\tYour final hand: {hands['player']["cards"]}, final score: {hands['player']["score"]}")
    print(f"\tComputer's final hand: {hands['computer']["cards"]}, final score: {hands['computer']["score"]}")

# procedure to judge who is winner
def judge():
    # one or both have score of 21
    if cdt_1 or cdt_2:
        if player_score != black_jack:
            print("You Lose😭 Computer has Blackjack.")
        elif computer_score != black_jack:
            print("You win with Blackjack😃")
        else:
            print("Both have Blackjack. Draw🙃")

    # one has score of over 21
    elif cdt_3 or cdt_4:
        if player_score > black_jack:
            print("You lose😭")
        elif computer_score > black_jack:
            print("You win😃")

    # both have score of under 21
    else:
        if player_score < computer_score:
            print("You lose😭")
        elif player_score > computer_score:
            print("You win😃")
        else:
            print("Draw🙃")

clear_screen()
while True:
    # database for each(play and computer)
    hands = {
            "player": {
                "cards": [],
                "score": 0
            },
            "computer": {
                "cards": [],
                "score": 0
            }
        }

    play = input("Do you want to play a game of Blackjack? Type y or n: ")
    if play != 'y':
        break
    else:
        clear_screen()
        print(art)
        hand_out()
        save_scores()
        player_score = hands["player"]["score"]
        computer_score = hands["computer"]["score"]

        # Magic Conditions
        cdt_1 = (player_score == black_jack)
        cdt_2 = (computer_score == black_jack)
        cdt_3 = (player_score > black_jack)
        cdt_4 = (computer_score > black_jack)

        if cdt_1 or cdt_2 or cdt_3 or cdt_4:
            show()
            decl_fnl_cond()
            judge()
            continue
        else:
            # Ask user to hit extra card or not, while user score < 21.
            while player_score <= black_jack:
                show()
                do_you_hit = input("Type 'y' to get another card, type 'n' to pass: ")
                if do_you_hit != 'y':
                    break
                else:
                    hit("player")
                    player_score = hands["player"]["score"]

        # Magic Conditions
        cdt_1 = (player_score == black_jack)
        cdt_2 = (computer_score == black_jack)
        cdt_3 = (player_score > black_jack)
        cdt_4 = (computer_score > black_jack)

        if cdt_1 or cdt_2 or cdt_3 or cdt_4:
            show()
            decl_fnl_cond()
            judge()
            continue
        else:
            while computer_score < computer_lmt:
                hit("computer")
                computer_score = hands["computer"]["score"]

        # Magic Conditions
        cdt_1 = (player_score == black_jack)
        cdt_2 = (computer_score == black_jack)
        cdt_3 = (player_score > black_jack)
        cdt_4 = (computer_score > black_jack)

        decl_fnl_cond()
        judge()
        continue

clear_screen()
