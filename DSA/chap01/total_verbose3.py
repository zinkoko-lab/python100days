# aからbまでの総和を求める（求める式も表示：その３）

print('aからbまでの総和を求めます。')
a = int(input('整数a：'))
b = int(input('整数b：'))

if a > b:
    a, b = b, a

print(*range(a, b + 1), sep=' + ', end=f' = {sum(range(a, b + 1))}\n')
