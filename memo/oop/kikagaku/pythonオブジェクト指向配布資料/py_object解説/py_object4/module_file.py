test = open("test111.text", "w")

test.write("テスト文章です。\nこんにちは")

test.close()

with open("test222.text", "w") as test222:
    test222.write("こんばんは。\nおやすみなさい。")

with open("test222.text", "r") as test222:
    print(test222.read())