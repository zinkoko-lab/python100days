import random

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

life_arts = [no_life, one_life, two_life, three_life, four_life, five_life, full_life]

def life_count(num_life):
    if num_life > 0:
        print(life_arts[num_life])
        print(f"****************************{num_life}/6 LIVES LEFT****************************")

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

placeholder = '_'*len(chosen_word)
placeholderLst = list(placeholder)
life = 6
guessed_Lst = []

while '_' in placeholderLst and life > 0:
    print(f"Word to guess: {placeholder}")
    guess = input("Guess the letter: ").lower()
    if not(guess in guessed_Lst) and guess in chosen_word:
        guessed_Lst.append(guess)
        cnt = 0
        for letter in chosen_word:
            if guess == letter:
                placeholderLst[cnt] = letter
            cnt += 1

        placeholder = ''
        for letter in placeholderLst:
            placeholder += letter
        life_count(life)

    elif guess in guessed_Lst:
        print(f"You've already guessed {guess}")
        life_count(life)

    else:
        life -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        life_count(life)

if life == 0:
    print(life_arts[life])
    print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")
else:
    print(f"***************YOU CAN GUESS THE WORD {chosen_word}! YOU WIN***************")

