# Does Python have Block Scope?

'''
# 例_1
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

# This is an example of "if block"
# The concept of code below is true for blocks except function blocks.
# The variables assigned within block except function block is counted as a global variable.
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)

'''

# 例_2
game_level = 10
enemies = ["Skeleton", "Zombie", "Alien"]

# This is an example of "function block"
# The variable assigned within an "if block" within a function block is counted as a local variable.
def create_enemy():
    new_enemy = "" # consider a safe side for game_level >= 5
    # If we don't assigned "new_enemy", NameError may be occurred under the condition game_level >= 5
    if game_level < 5:
        new_enemy = enemies[0]
    print(new_enemy)

create_enemy() # game_level = 10 >= 5 ... new_enemy = ""
# print(new_enemy) # This line output an error like: NameError: name 'new_enemy' is not defined
