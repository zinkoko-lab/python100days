# 配列の要素の最大値を求めて表示（要素の値を乱数で生成）

import random
from max import max_of

print('乱数の最大値を求めます。')
no = int(input('乱数の個数：'))
lo = int(input('乱数の下限：'))
hi = int(input('乱数の上限：'))
x = [None] * no     # 要素数noのリストを生成

for i in range(no):
    x[i] = random.randint(lo, hi)

print(x)
print(f'最大値は{max_of(x)}です。')
