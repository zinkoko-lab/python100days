import random
import os
from logo import art

# ターミナルの画面をクリアする関数を定義
# os.name が 'nt' の場合は Windows ⇒ 'cls' コマンド
# それ以外（macOS / Linux）の場合は 'clear' コマンドを使用
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# global constants
DECK = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
INIT_HANDOUT = 2    # initial handout is two cards for each
ACE = 11            # original ace
ALT_ACE = 1         # alternative ace
MAGIC_NUMBER = 12   # magic number from my logical thinking
BLACK_JACK = 21     # ultimate score
COMPUTER_LMT = 17   # after user's hit, computer consider hit or not base upon this limit score

# At start, EVERYTHING is empty:
player = {}
computer = {}
hands = {}
magic_conditions = []

# Function to reset info
def reset_hands():
    player["cards"] = []
    player["score"] = 0
    computer["cards"] = []
    computer["score"] = 0
    hands["player"] = player
    hands["computer"] = computer

# Magic Conditions
def check_magic_conditions():
    global magic_conditions
    cdt_0 = (player["score"] == BLACK_JACK)
    cdt_1 = (computer["score"] == BLACK_JACK)
    cdt_2 = (player["score"] > BLACK_JACK)
    cdt_3 = (computer["score"] > BLACK_JACK)
    magic_conditions = [cdt_0, cdt_1, cdt_2, cdt_3]
    return sum(magic_conditions)

# function to calculate score
def calc_score(cards: list):
    dummy_lst = []
    if ACE in cards:
        ace_cnt = cards.count(ACE)
        score_lmt = MAGIC_NUMBER - ace_cnt
        score_without_ace = sum([_ for _ in cards if _ != ACE])
        if score_without_ace >= score_lmt:
            for card in cards:
                if card == ACE:
                    dummy_lst.append(ALT_ACE)
                else:
                    dummy_lst.append(card)
        else:
            first_ace_idx = cards.index(ACE)
            for idx in range(len(cards)):
                if idx != first_ace_idx:
                    if cards[idx] == ACE:
                        dummy_lst.append(ALT_ACE)
                    else:
                        dummy_lst.append(cards[idx])
                else:
                    dummy_lst.append(cards[idx])
    else:
        dummy_lst = cards

    return sum(dummy_lst)

# procedure to hand out each two cards for each and update the database
def hand_out():
    for _ in range(INIT_HANDOUT):
        player["cards"].append(random.choice(DECK))
        computer["cards"].append(random.choice(DECK))
        player["score"] = calc_score(player["cards"])
        computer["score"] = calc_score(computer["cards"])
        hands["player"] = player
        hands["computer"] = computer

# procedure of to hit and update the database
def hit(who: str):
    players = list(hands.keys())
    player_idx = players.index("player")
    computer_idx = players.index("computer")
    if who in players:
        idx = players.index(who)
        if idx == player_idx:
            player["cards"].append(random.choice(DECK))
            player["score"] = calc_score(player["cards"])
            hands["player"] = player
        else:
            computer["cards"].append(random.choice(DECK))
            computer["score"] = calc_score(computer["cards"])
            hands["computer"] = computer

# procedure to show all the player's cards and score
# and show the first card of computer
def show_player_state():
        print(f"\tYour cards: {player["cards"]}, current score: {player["score"]}")
        print(f"\tComputer's first card: {computer["cards"][0]}")

# procedure to declare final condition
def decl_fnl_cond():
    print(f"\tYour final hand: {player["cards"]}, final score: {player["score"]}")
    print(f"\tComputer's final hand: {computer["cards"]}, final score: {computer["score"]}")
    print("\n")

# procedure to judge who is winner
def declare_winner_under_magic_conditions():
    cdt_0 = magic_conditions[0]
    cdt_1 = magic_conditions[1]
    cdt_2 = magic_conditions[2]
    cdt_3 = magic_conditions[3]
    # one or both have score of 21
    if cdt_0 or cdt_1:
        if player["score"] != BLACK_JACK:
            print("You Lose😭 Computer has Blackjack.")
        elif computer["score"] != BLACK_JACK:
            print("You win with Blackjack😃")
        else:
            print("Both have Blackjack. Draw🙃")
    # one has score of over 21
    elif cdt_2 or cdt_3:
        if player["score"] > BLACK_JACK:
            print("You lose😭")
        elif computer["score"] > BLACK_JACK:
            print("You win😃")

    # both have score of under 21
def declare_winner_under_normal_condition():
    if player["score"] < computer["score"]:
        print("You lose😭")
    elif player["score"] > computer["score"]:
        print("You win😃")
    else:
        print("Draw🙃")

clear_screen()
while True:
    # reset the database
    reset_hands()

    play = input("Do you want to play a game of Blackjack? Type y or n: ").lower()
    if play != 'y':
        clear_screen()
        break
    else:
        clear_screen()
        print(art)
        hand_out()

        if check_magic_conditions():
            show_player_state()
            decl_fnl_cond()
            declare_winner_under_magic_conditions()
            continue
        else:
            # Ask user to hit extra card or not, while user score < 21.
            while player["score"] <= BLACK_JACK:
                show_player_state()
                do_you_hit = input("Type 'y' to get another card, type 'n' to pass: ").lower()
                if do_you_hit != 'y':
                    break
                else:
                    hit("player")

        if check_magic_conditions():
            show_player_state()
            decl_fnl_cond()
            declare_winner_under_magic_conditions()
            continue
        else:
            while computer["score"] < COMPUTER_LMT:
                hit("computer")

        show_player_state()
        decl_fnl_cond()
        if check_magic_conditions():
            declare_winner_under_magic_conditions()
        else:
            declare_winner_under_normal_condition()
            continue
