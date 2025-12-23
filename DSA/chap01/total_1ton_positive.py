# 1からnまでの総和を求める（nに正の整数値を読み込む）

print('1からnまでの総和を求めます。')

while True:
    n = int(input('nの値：'))
    if n > 0:
        break

total = 0

for i in range(1, n + 1):
    total += i  # totalにiを加える

print(f'1から{n}までの総和は{total}です。')
