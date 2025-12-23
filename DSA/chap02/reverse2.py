# 配列（リスト）の要素の並びを反転（reverseメソッド）

print('配列の要素の並びを反転します。')
nx = int(input('要素数は：'))
x = [None] * nx    # 要素数nxのリストを生成

for i in range(nx):
    x[i] = int(input(f'x[{i}] : '))

x.reverse()        # xの並びを反転

print('配列の要素の並びを反転しました。')
for i in range(nx):
    print(f'x[{i}] = {x[i]}')
