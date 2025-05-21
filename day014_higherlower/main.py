from random import choice
import art
from game_data import data

# =================================================================

# generate a number for data_A and pop from the index list
# index for data A = index list.pot(choice(index list))

# generate a number for data_B and pop from the index list
# index for data B = index list.pot(choice(index list))

# use index for data A and B to play the game

# If the player alive:

# index for data A = index for data B

# generate a number for data_B and pop from the index list
# index for data B = index list.pot(choice(index list))

# use index for data A and B to play the game

# If the player alive:

# index for data A = index for data B

# generate a number for data_B and pop from the index list
# index for data B = index list.pot(choice(index list))

# use index for data A and B to play the game

# else:

# game is over

# =================================================================

ref_idx = list(range(len(data)))
print(ref_idx)

def generate_rdn_idx():
    return ref_idx.pop(choice(ref_idx))

print(f"length of ref_idx: {len(ref_idx)}")

idx_for_data_a = generate_rdn_idx()

print(f"idx for A: {idx_for_data_a}")

print(f"length of ref_idx: {len(ref_idx)}")

idx_for_data_b = generate_rdn_idx()

print(f"idx for B: {idx_for_data_b}")

print(f"length of ref_idx: {len(ref_idx)}")
