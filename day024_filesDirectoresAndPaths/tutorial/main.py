# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

with open("my_file.txt", mode="a+") as f:
    f.seek(0)  # 先頭に戻る（a+モードでは必須）
    # なぜ f.seek(0) が必要なのか？
    # •	a+ モードではファイルポインタ（読み書きの位置）が 常に末尾にある。
    # •	そのため、read() や readlines() を使っても、最初に f.seek(0) をしないと何も読み込まれません。
    contents = f.readlines()
    for sentence in contents:
        print(sentence.strip())

    f.write("\nYoroshiku.")

with open("my_file.txt", mode="a+") as f:
    f.seek(0)
    for sentence in contents:
        print(sentence.strip())
