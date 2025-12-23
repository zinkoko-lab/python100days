# 1からnまでの総和を求める（range関数＋sum関数）

print('1からnまでの総和を求めます。')
n = int(input('nの値：'))

print(f'1から{n}までの総和は{sum(range(1, n + 1))}です。')
