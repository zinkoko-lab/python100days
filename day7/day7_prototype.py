word = "aeroplane"
word = list(word)
life = 6
while len(word) > 0 and life > 0:
    letter = input("Guess the letter: ")
    if letter in word:
        word.remove(letter)
        print(f"You guessed \'{letter}\' is ture.")
        print(word)
        print(f"life = {life}/6")
        if len(word) == 0:
            print("You win!")
    else:
        print(f"You guessed {letter}, that's not in the word. You lose a life.")
        life -= 1
        print(f"life = {life}/6")
        if life == 0:
            print("You lose")