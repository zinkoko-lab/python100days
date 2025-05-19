print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************

Welcome to Treasure Island.
Your mission is to find the treasure.
You're at a cross road. Where do you want to go?

''')
flag1 = False
while not flag1:
    direction = input("Type 'left' or 'right': ").lower()
    if direction == "left":
        flag1 = True
        print('''
        You've come to a lake. 
        There is an island in the middle of the lake.
        ''')
        flag2 = False
        while not flag2:
            swimOr_Wait = input("Type 'wait' to wait for a boat. Type 'swim' to swim across.: ").lower()
            if swimOr_Wait == "wait":
                flag2 = True
                print('''
                You arrive at the island unharmed. 
                There is a house with 3 doors.
                One red, one yellow and one blue. 
                Which colour do you choose?
                ''')
                flag3 = False
                while not flag3:
                    whichDoor = input("Type 'yellow' or 'blue': ").lower()
                    if whichDoor == "yellow":
                        flag3 = True
                        print("You found the treasure💎 and win🎉")
                    elif whichDoor == "blue":
                        flag3 = True
                        print("You enter a room of beasts. Game Over.")
                    else:
                        flag3 = False
                        print("You typed wrong input.")
            elif swimOr_Wait == "swim":
                flag2 = True
                print("You get attacked by an angry trout. Game Over.")
            else:
                flag2 = False
                print("You typed wrong input.")
    elif direction == "right":
        flag1 = True
        print("You fell into a hole. Game Over.")
    else:
        flag1 = False
        print("You typed wrong input.")
