# 最大公約数を求める（math.gcdを利用）

import math

print('二つの整数の最大公約数を求めます。')
x = int(input('整数：'))
y = int(input('整数：'))

print(f'最大公約数は{math.gcd(x, y)}です。')
