# ファイルの全てを読み込む
# with open("test.txt") as f:
#     s = f.read()
#     print(s)

# ファイルの1行ずつを読み込む
# with open("test.txt") as f:
#     for _ in range(10):
#         s_line = f.readline()
# print(s_line)
# print(s_line, end="") # printによる改行を抑制
# print(s_line.strip()) # 改行を削除して表示
# if s_line == "":
#     print("終了です。")
#     break
"""
•	readline()はファイルの1行を「そのまま」（改行文字付きで）返します。
•	print()は改行を追加します。
•	この二重の改行が「行間が空いた」ように見える原因です。
"""

# ファイルを1行をリストの要素一つとして読み込む
# with open("test.txt") as f:
#     s_line = f.readlines()
#     print(s_line)

# 新しいファイルを作成し、文字を書き込む
# with open("test2.txt", "w") as f:
#     f.write("あああ\nいいい\nううう")

# 上記のコードで作ったファイルに文字を追記する
# with open("test2.txt", "a") as f:
#     f.write("\nえええ\nおおお")

fruits = ["apple", "orange", "banana"]
s = "\n".join(fruits)
print(s)

with open("test3.txt", "w") as f:
    f.write(s)
