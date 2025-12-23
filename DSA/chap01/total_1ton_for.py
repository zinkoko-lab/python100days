# 1からnまでの総和を求める（for文）

print('1からnまでの総和を求めます。')
n = int(input('nの値：'))

total = 0
for i in range(1, n + 1):
    total += i  # totalにiを加える

print(f'1から{n}までの総和は{total}です。')
