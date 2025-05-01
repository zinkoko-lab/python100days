import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

placeholder = '_'*len(chosen_word)
placeholderLst = list(placeholder)

while '_' in placeholderLst:
    guess = input("Guess the letter: ").lower()

    cnt = 0
    for letter in chosen_word:
        if guess == letter:
            placeholderLst[cnt] = letter
        cnt += 1

    placeholder = ''
    for letter in placeholderLst:
        placeholder += letter
    print(placeholder)