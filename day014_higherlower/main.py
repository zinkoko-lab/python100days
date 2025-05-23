from random import choice
import os
import art
from game_data import data

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def two_rdm_data(prev_lst: list):
    idx_lst = list(range(len(data)))
    next_lst = list()
    if len(prev_lst) == 0:
        for _ in range(2):
            tmp_idx = choice(idx_lst)
            idx_lst.remove(tmp_idx)
            next_lst.append(data[tmp_idx])
    else:
        next_lst.append(prev_lst[-1])
        for i in range(2):
            tmp_idx = data.index(prev_lst[i])
            idx_lst.remove(tmp_idx)
        next_lst.append(data[choice(idx_lst)])

    return next_lst

def describe_data(who: dict):
    print(f"{who['name']}, ", end = '')
    # print(f"{who['follower_count']}, ", end = '')
    print(f"{who['description']}, ", end = '')
    print(f"from {who['country']}.")

a_and_b = list()
result = True
score = 0

while result:
    a_and_b = two_rdm_data(a_and_b)
    data_a, data_b = a_and_b

    clear_screen()
    print(art.logo)
    if score > 0:
        print(f"You're right! Current score: {score}")

    print(f"Compare A: ", end='')
    describe_data(data_a)
    print(art.vs)
    print(f"Against B: ", end='')
    describe_data(data_b)

    ab_follower_cnt = {
        'a': data_a["follower_count"],
        'b': data_b["follower_count"]
    }

    a_or_b = input("Who has more followers? Type 'A' or 'B': ").lower()
    if a_or_b == 'a':
        result = ab_follower_cnt[a_or_b] > ab_follower_cnt['b']
    elif a_or_b == 'b':
        result = ab_follower_cnt[a_or_b] > ab_follower_cnt['a']
    else:
        result = False

    if result == True:
        score += 1

clear_screen()
print(art.logo)
print(f"Sorry, that's wrong. Final score: {score}")
