# 多値の最大公約数を求める

import math

print('多値の最大公約数を求めます。')
num = int(input('要素数：'))
x = [None] * num    # 要素数numの配列を生成

for i in range(num):
    x[i] = int(input(f'x[{i}] : '))

print(f'最大公約数は{math.gcd(*x)}です。')
