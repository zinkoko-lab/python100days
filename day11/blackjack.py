#!/usr/bin/env python3
import random
import os
from logo import art

# ターミナルをクリアする関数（Windows は 'cls'、それ以外は 'clear' を使用）
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# ゲーム内定数
DECK = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
INIT_HANDOUT = 2    # 初期配布カード数
ACE = 11            # エースのデフォルト値
ALT_ACE = 1         # エースがバースト回避で1としてカウントされる場合
MAGIC_NUMBER = 12   # エース調整用の閾値
BLACK_JACK = 21     # ブラックジャックの点数
COMPUTER_LMT = 17   # コンピューターがヒットするかの判断基準スコア

# プレイヤーとコンピュータの状態（カードとスコア）を格納
player = {}
computer = {}
hands = {}
magic_conditions = []

# プレイヤーとコンピュータの状態を初期化
def reset_hands():
    player["cards"] = []
    player["score"] = 0
    computer["cards"] = []
    computer["score"] = 0
    hands["player"] = player
    hands["computer"] = computer

# 勝敗に関わる条件（ブラックジャック or バースト）をチェック
def check_magic_conditions(player_score: int, computer_score: int):
    global magic_conditions
    cdt_0 = (player_score == BLACK_JACK)
    cdt_1 = (computer_score == BLACK_JACK)
    cdt_2 = (player_score > BLACK_JACK)
    cdt_3 = (computer_score > BLACK_JACK)
    magic_conditions = [cdt_0, cdt_1, cdt_2, cdt_3]
    return sum(magic_conditions)

# カードのスコア計算（エースの調整を含む）
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

# 最初に各プレイヤーに2枚ずつカードを配る
def hand_out():
    for _ in range(INIT_HANDOUT):
        player["cards"].append(random.choice(DECK))
        computer["cards"].append(random.choice(DECK))
        player["score"] = calc_score(player["cards"])
        computer["score"] = calc_score(computer["cards"])
        hands["player"] = player
        hands["computer"] = computer

# 指定されたプレイヤー（playerまたはcomputer）にカードを1枚追加
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

# プレイヤーのカードとスコア、コンピュータの1枚目のカードを表示
def show_player_state():
        print(f"\tYour cards: {player["cards"]}, current score: {player["score"]}")
        print(f"\tComputer's first card: {computer["cards"][0]}")

# ゲーム終了時に両者のカードとスコアを表示ｓ
def declare_final_condition():
    print(f"\tYour final hand: {player["cards"]}, final score: {player["score"]}")
    print(f"\tComputer's final hand: {computer["cards"]}, final score: {computer["score"]}")
    print("\n")

# ブラックジャックやバーストがあった場合の勝敗判定
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

# 通常条件下での勝敗判定（ブラックジャックでもバーストでもない）
def declare_winner_under_normal_condition():
    if player["score"] < computer["score"]:
        print("You lose😭")
    elif player["score"] > computer["score"]:
        print("You win😃")
    else:
        print("Draw🙃")

# -------------------------------
# メインゲームループ開始
# -------------------------------
clear_screen()
while True:
    reset_hands()   # 状態の初期化

    play = input("Do you want to play a game of Blackjack? Type y or n: ").lower()
    if play != 'y':
        clear_screen()
        break
    else:
        clear_screen()
        print(art)
        hand_out()

        # 最初の2枚でブラックジャックやバーストかどうか判定
        if check_magic_conditions(player["score"], computer["score"]):
            show_player_state()
            declare_final_condition()
            declare_winner_under_magic_conditions()
            continue

        # Ask user to hit extra card or not, while user score < 21.
        while player["score"] <= BLACK_JACK:
            show_player_state()
            do_you_hit = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if do_you_hit != 'y':
                break
            else:
                hit("player")

        # プレイヤーがヒットするかどうか判断
        if check_magic_conditions(player["score"], computer["score"]):
            show_player_state()
            declare_final_condition()
            declare_winner_under_magic_conditions()
            continue

        # コンピューターが17未満ならヒット
        while computer["score"] < COMPUTER_LMT:
            hit("computer")

        show_player_state()
        declare_final_condition()
        if check_magic_conditions(player["score"], computer["score"]):
            declare_winner_under_magic_conditions()
            continue

        # 通常勝負
        declare_winner_under_normal_condition()
        continue
