# Scope

# 例_1
# Global Scope
enemies = 1

def increase_enemies():
    # This is Local Scope
    enemies = 2
    print(f"enemies inside the function: {enemies}")

increase_enemies()

print(f"enemies outside the function; {enemies}")

# To increase the enemies outside the function(Global Scope)
def increase_enemies_globally():
    # Need to declare the variable 'enemies' as 'global'
    global enemies
    enemies = 5

increase_enemies_globally()
print(f"After increasing enemies globally: enemies = {enemies}")

# 例_2
# Local Scope

def drink_portion():
    global portion_strength
    portion_strength = 2
    print(portion_strength)

drink_portion()

# If you didn't declare 'portion_strength' as global,
# the result of the next line is error like:
# NameError: name 'portion_strength' is not defined
# comment out the line 'global portion_strength' in drink_portion function
print(portion_strength)

# 例_3
# Global variable can be access from everywhere
# Local functions i.e functions inside the a global functions
# Local functions cannot be access from everywhere(accessible only in parent function)
player_health = 10      # This is global variable

def player_condition():
    def display_player_health():    # This is local function
        print(player_health)        # This is calling out the global variable

player_condition()  # This is calling out the global function

# display_player_health() # This is calling out the local function -> error like:
# NameError: name 'display_player_health' is not defined
