print("ゼロ除算エラーをテストするプログラムです")
while True:
    a = float(input("1つ目の数値を入力してください: "))
    b = float(input("2つ目の数値を入力してください: "))
    try:
        c = a / b
        print(c)
        break
    except ZeroDivisionError:
        print("入力した数値が不適切です")
