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

# At start, nothing is empty:
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
    cdt_0 = (player["score"] == black_jack)
    cdt_1 = (computer["score"] == black_jack)
    cdt_2 = (player["score"] > black_jack)
    cdt_3 = (computer["score"] > black_jack)
    magic_conditions = [cdt_0, cdt_1, cdt_2, cdt_3]
    return sum(magic_conditions)

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

# procedure to hand out each two cards for each and update the database
def hand_out():
    for _ in range(init_handout):
        player["cards"].append(random.choice(deck))
        computer["cards"].append(random.choice(deck))
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
            player["cards"].append(random.choice(deck))
            player["score"] = calc_score(player["cards"])
            hands["player"] = player
        else:
            computer["cards"].append(random.choice(deck))
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
        if player["score"] != black_jack:
            print("You Lose😭 Computer has Blackjack.")
        elif computer["score"] != black_jack:
            print("You win with Blackjack😃")
        else:
            print("Both have Blackjack. Draw🙃")
    # one has score of over 21
    elif cdt_2 or cdt_3:
        if player["score"] > black_jack:
            print("You lose😭")
        elif computer["score"] > black_jack:
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

    play = input("Do you want to play a game of Blackjack? Type y or n: ")
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
            while player["score"] <= black_jack:
                show_player_state()
                do_you_hit = input("Type 'y' to get another card, type 'n' to pass: ")
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
            while computer["score"] < computer_lmt:
                hit("computer")

        show_player_state()
        decl_fnl_cond()
        if check_magic_conditions():
            declare_winner_under_magic_conditions()
        else:
            declare_winner_under_normal_condition()
            continue
