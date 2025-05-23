from random import choice
import os
import art
from game_data import data

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def two_rdm_data(prev_lst: list):
    """Generate a list of two random data
    from the variable of game_data.py."""

    # assign a list that contains elements, each represents
    # the index number of game_data.data
    idx_lst = list(range(len(data)))

    # assign a blank list that's finally return as a result list.
    next_lst = list()

    # at the start of game, there is no data to play.
    # Under such condition, this function can generate a list of
    # two random data.
    if len(prev_lst) == 0:
        for _ in range(2):
            tmp_idx = choice(idx_lst)
            idx_lst.remove(tmp_idx)
            next_lst.append(data[tmp_idx])
    else:
        # in case of data list contain two:
        # remove the first data of the list
        # reuse the second data of the list as first data
        # add a random data as second data
        next_lst.append(prev_lst[-1])
        for i in range(2):
            tmp_idx = data.index(prev_lst[i])
            idx_lst.remove(tmp_idx)
        next_lst.append(data[choice(idx_lst)])

    return next_lst

def describe_data(who: dict):
    """Show the name, description, and country of the data.
    """
    print(f"{who['name']}, ", end = '')
    # print(f"{who['follower_count']}, ", end = '') # for test
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
