# シーケンスの要素の最大値を表示する（組込みのmax関数を利用）

print('配列の最大値を求めます。')
num = int(input('要素数：'))
x = [None] * num  # 要素数numのリストを生成

for i in range(num):
    x[i] = int(input(f'x[{i}]：'))

print(f'最大値は{max(x)}です。')
