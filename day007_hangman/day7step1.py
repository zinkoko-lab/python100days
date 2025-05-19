import random
word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from word_list and
#  assign it to a variable called chosen_word. Then print it.
# random_idx = random.randint(0, len(word_list)-1)
# chosen_word = word_list[random_idx]
chosen_word = random.choice(word_list)

# TODO-2 - Ask the user to guess a letter and assign their answer
#  to a variable called guess. Make guess lowercase.
guess = input("Guess the letter: ").lower()

# TODO-3 - Check if the letter the user guessed (guess) is
#  one of the letter in the chosen_word. Print "Right" if it is,
#  "Wrong" if it's not.
# for idx in range(len(chosen_word)):
#     if guess == chosen_word[idx]:
#         print("Right")
#     else:
#         print("Wrong")
for letter in chosen_word:
    if guess == letter:
        print("Right")
    else:
        print("Wrong")