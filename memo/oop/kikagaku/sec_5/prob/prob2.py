print("ゼロ除算エラーとValueErrorをテストするプログラムです")
while True:
    try:
        a = float(input("1つ目の数値を入力してください: "))
        b = float(input("2つ目の数値を入力してください: "))
        c = a / b
        print(c)
        break
    except ZeroDivisionError:
        print("0 で割れません")
    except ValueError:
        print("数値を入力してください")
    except:
        print("その他の例外が発生しました")
