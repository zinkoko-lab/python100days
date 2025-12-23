# 非負の整数の階乗値を求める（math.factorialを利用）

import math

n = int(input('何の階乗：'))
try:
    print(f'{n}の階乗は{math.factorial(n)}です。')
except ValueError:
    print(f'{n}の階乗は求められませんでした。')
