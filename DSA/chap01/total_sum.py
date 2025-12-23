# aからbまでの総和を求める（range関数＋sum関数）

print('aからbまでの総和を求めます。')
a = int(input('整数a：'))
b = int(input('整数b：'))

if a > b:
    a, b = b, a

print(f'{a}から{b}までの総和は{sum(range(a, b + 1))}です。')
