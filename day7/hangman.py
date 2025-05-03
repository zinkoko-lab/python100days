#!/usr/bin/env python3
import random

# タイトルアートの表示
print(r'''
_                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/
''')

# ハングマンの各段階のアート（ライフ数に応じて表示）
full_life = r'''
 +---+
  |   |
      |
      |
      |
      |
=========
'''
five_life = r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
'''
four_life = r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
'''
three_life = r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
'''
two_life = r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
'''
one_life = r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
'''
no_life = r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
'''

# ライフ数に応じて使うアートをリストにまとめる（インデックスで呼び出し）
life_arts = [no_life, one_life, two_life, three_life, four_life, five_life, full_life]

# ライフ数をもとにアートと残りライフを表示する関数
def life_count(num_life):
    if num_life > 0:
        print(life_arts[num_life])
        print(f"****************************{num_life}/6 LIVES LEFT****************************")

# ランダムに単語を選択し、プレースホルダーを初期化
word_list = [
    "aardvark", "baboon", "camel", "python", "giraffe", "elephant", "kangaroo",
    "dolphin", "tiger", "leopard", "zebra", "ostrich", "flamingo", "peacock",
    "raccoon", "panda", "hippopotamus", "crocodile", "alligator", "cheetah",
    "antelope", "buffalo", "porcupine", "armadillo", "koala", "walrus", "otter",
    "badger", "moose", "reindeer", "sloth", "turkey", "hedgehog", "squirrel",
    "beaver", "parrot", "chicken", "goose", "donkey", "monkey", "rabbit", "horse",
    "snake", "shark", "whale", "eagle", "falcon", "penguin", "bear", "fox", "wolf",
    "lion", "rhino", "bat", "frog", "lizard", "snail", "crab", "octopus", "squid"
]
chosen_word = random.choice(word_list)

placeholder = '_' * len(chosen_word)
placeholderLst = list(placeholder)
life = 6
guessed_Lst = []

# メインのゲームループ：単語を当てるかライフが尽きるまで繰り返す
while '_' in placeholderLst and life > 0:
    print(f"Word to guess: {placeholder}")
    guess = input("Guess the letter: ").lower()

    # 正しい文字を初めて当てた場合
    if not(guess in guessed_Lst) and guess in chosen_word:
        guessed_Lst.append(guess)
        cnt = 0
        for letter in chosen_word:
            if guess == letter:
                placeholderLst[cnt] = letter
            cnt += 1

        # 更新したプレースホルダーを文字列に戻す
        placeholder = ''
        for letter in placeholderLst:
            placeholder += letter
        life_count(life)

    # すでに推測した文字だった場合
    elif guess in guessed_Lst:
        print(f"You've already guessed {guess}")
        life_count(life)

    # 外れた場合
    else:
        life -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        life_count(life)

# 勝敗結果の表示
if life == 0:
    print(life_arts[life])
    print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")
else:
    print(f"***************YOU CAN GUESS THE WORD {chosen_word}! YOU WIN***************")