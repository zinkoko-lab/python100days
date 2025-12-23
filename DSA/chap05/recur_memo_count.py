# 真に再帰的な関数recurをメモ化して実現（呼び出し回数をカウント）

counter = 0         # 関数recurの呼び出し回数

memo = [''] * 128                       # メモ用文字列の配列

def recur(n: int) -> None:
    """メモ化を導入した関数recur"""
    global counter
    counter += 1
    if memo[n + 1] != '':
        print(memo[n + 1], end='')      # メモを出力
    else:
        if n > 0:
            recur(n - 1)
            print(n)
            recur(n - 2)
            memo[n + 1] = f'{memo[n]}{n}\n{memo[n - 1]}'
        else:
            memo[n + 1] = ''

x = int(input('整数を入力せよ：'))

recur(x)

print(f'関数recurは{counter}回呼び出されました。')
