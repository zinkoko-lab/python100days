try:
    print("test")
    # int("100")
    int("hundred")
except ValueError:
    print("例外が発生しました")
else:
    print("例外が発生しませんでした")
finally:
    print("例外の発生に関わらず実行")
