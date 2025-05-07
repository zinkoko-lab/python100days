#!/usr/bin/env python3
art = r'''
        
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88           
'''

print(art)

def encode(plain_text: str, key: int):
    encoded_text = ''
    for letter in plain_text:
        if letter.isalpha():
            if letter.isupper():
                encoded_text += chr(ord('A') + (ord(letter) - ord('A') + key) % 26)
            else:
                encoded_text += chr(ord('a') + (ord(letter) - ord('a') + key) % 26)
        else:
            encoded_text += letter

    return encoded_text

def decode(encoded_text: str, key: int):
    decoded_text = ''
    for letter in encoded_text:
        if letter.isalpha():
            if letter.isupper():
                decoded_text += chr(ord('Z') - (ord('Z') - ord(letter) + key) % 26)
            else:
                decoded_text += chr(ord('z') - (ord('z') - ord(letter) + key) % 26)
        else:
            decoded_text += letter

    return decoded_text

again = 'yes'

while again == 'yes':

    flag = False
    while not flag:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        if direction == 'encode' or direction == 'decode':
            flag = True

    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))

    if direction == 'encode':
        print(encode(text, shift))
    elif direction == "decode":
        print(decode(text, shift))
    else:
        pass

    again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
