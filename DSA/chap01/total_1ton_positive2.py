# 1からnまでの総和を求める（nに正の整数値を読み込む：代入演算子:=を利用）

print('1からnまでの総和を求めます。')

while (n := int(input('nの値：'))) <= 0:
    pass

total = 0

for i in range(1, n + 1):
    total += i  # totalにiを加える

print(f'1から{n}までの総和は{total}です。')
