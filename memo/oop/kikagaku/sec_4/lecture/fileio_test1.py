with open("test222.txt", "w") as test222:
    test222.write("こんにちは。\nおやすみなさい。")

with open("test222.txt", "r") as test222:
    s_line = test222.readlines()

for s_l in s_line:
    print(s_l.strip())

with open("test222.txt", "a") as test222:
    test222.write("\nAAA\nBBB\nCCC")

with open("test222.txt", "r") as test222:
    s_line = test222.readlines()

for s_l in s_line:
    print(s_l.strip())
