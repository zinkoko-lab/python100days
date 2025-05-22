from random import choice
import os
import art
from game_data import data

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_two_rdm_index(previous_lst: list):
    lst_of_idx = list(range(len(data)))
    for i in range(len(previous_lst)):
        if previous_lst[i] in lst_of_idx:
            lst_of_idx.remove(previous_lst[i])
    if len(previous_lst) == 2:
        previous_lst.remove(previous_lst[0])
        previous_lst.append(choice(lst_of_idx))
    else:
        for _ in range(2):
            previous_lst.append(choice(lst_of_idx))
    return previous_lst

rdm_idx = list()
result = True
score = 0

while result:
    rdm_idx = generate_two_rdm_index(rdm_idx)
    # for data A,
    data_a = data[rdm_idx[0]]
    name_a = data_a["name"]
    flr_cnt_a = data_a["follower_count"]
    des_a = data_a["description"]
    country_a = data_a["country"]

    # for data A,
    data_b = data[rdm_idx[1]]
    name_b = data_b["name"]
    flr_cnt_b = data_b["follower_count"]
    des_b = data_b["description"]
    country_b = data_b["country"]

    clear_screen()
    print(art.logo)
    if score > 0:
        print(f"You're right! Current score: {score}")
    print(f"Compare A: {name_a}, {des_a}, from {country_a}.")

    print(art.vs)

    print(f"Against B: {name_b}, {des_b}, from {country_b}.")

    if flr_cnt_a > flr_cnt_b:
        who_is_higher = 'a'
    else:
        who_is_higher = 'b'

    user_input = input("Who has more followers? Type 'A' or 'B': ").lower()

    if user_input == who_is_higher:
        result = True
        score += 1
    else:
        result = False

clear_screen()
print(art.logo)
print(f"Sorry, that's wrong. Final score: {score}")
