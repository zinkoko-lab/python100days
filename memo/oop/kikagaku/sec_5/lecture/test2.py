"""
書式 -> except節、finally節

try:
    例外が発生する可能性がある処理
except:
    例外が発生した時の処理
else:
    例外が発生しなかった時の処理
finally:
    例外が発生しても、しなくてする処理

"""

try:
    print("test")
    # int("ten")
    int("100")
except ValueError:
    print("例外が発生しました。")
else:
    print("例外が発生しませんでした。")
finally:
    print("例外の発生にかかわらず実行")
