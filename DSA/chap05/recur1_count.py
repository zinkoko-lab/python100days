# 真に再帰的な関数（呼び出し回数をカウント）

counter = 0         # 関数recurの呼び出し回数

def recur(n: int) -> None:
    """真に再帰的な関数recur"""
    global counter
    counter += 1
    if n > 0:
        recur(n - 1)
        print(n)
        recur(n - 2)

x = int(input('整数を入力せよ：'))

recur(x)

print(f'関数recurは{counter}回呼び出されました。')
