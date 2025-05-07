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
    """
        テキストをシーザー暗号でエンコードする。

        Args:
            plain_text (str): エンコード対象の文字列
            key (int): シフトする文字数

        Returns:
            str: エンコードされた文字列
    """
    encoded_text = ''
    for letter in plain_text:
        if letter.isalpha():    # アルファベットの場合のみデコード処理を行う
            # 大文字の場合
            if letter.isupper():
                encoded_text += chr(ord('A') + (ord(letter) - ord('A') + key) % 26)     # シフト後の文字を計算
            # 小文字の場合
            else:
                encoded_text += chr(ord('a') + (ord(letter) - ord('a') + key) % 26)
        # アルファベット以外はそのまま追加
        else:
            encoded_text += letter

    return encoded_text

def decode(encoded_text: str, key: int):
    """
        シーザー暗号をデコードする。

        Args:
            encoded_text (str): デコード対象の文字列
            key (int): シフトする文字数

        Returns:
            str: デコードされた文字列
    """
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


# メインループ
while True:
    # テキストを暗号化する復号化するかユーザーに選択させる
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction not in ['encode', 'decode']:
        print("Invalid option. Please type 'encode' or 'decode'.")
        continue

    # ユーザーに暗号化してほしいまたは復号化してほしいテキストを入力させる
    text = input("Type your message:\n")

    try:
        shift = int(input("Type the shift number:\n")) % 26
    except ValueError:
        print("Shift must be an integer.")
        continue

    # 選択に応じてエンコードまたはデコードを実行
    if direction == 'encode':
        print(encode(text, shift))
    elif direction == "decode":
        print(decode(text, shift))

    # もう一度実行するか尋ねる
    again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if again != 'yes':
        print("Goodbye")
        break
