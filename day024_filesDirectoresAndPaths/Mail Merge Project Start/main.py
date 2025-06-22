with open(file="./Input/Names/invited_names.txt") as invited_names:
    name_data = invited_names.readlines()
    names = []
    for name in name_data:
        names.append(name.strip())

with open(file="./Input/Letters/starting_letter.txt") as letter:
    text = letter.read()

for name in names:
    new_text = text.replace("[name]", name)
    new_file_name = f"letter_for_{name}.txt"
    with open(file=f"./Output/ReadyToSend/{new_file_name}", mode="w") as f:
        f.write(new_text)


# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
