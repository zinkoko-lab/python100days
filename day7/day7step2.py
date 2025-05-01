import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

placeholder = '_'*len(chosen_word)
placeholderLst = list(placeholder)
life = 6
guessed_Lst = []

while '_' in placeholderLst and life > 0:
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
        print(placeholder)
        print(guessed_Lst)
        print(f"life = {life}/6")
    else:
        life -= 1
        print(placeholder)
        print(guessed_Lst)
        print(f"life = {life}/6")


