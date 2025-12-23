# 配列（リスト）の要素の並びを反転（reversed関数＋list関数）

print('配列の要素の並びを反転します。')
nx = int(input('要素数は：'))
x = [None] * nx    # 要素数nxのリストを生成

for i in range(nx):
    x[i] = int(input(f'x[{i}] : '))

y = list(reversed(x))   # リストxの要素の並びを反転したリストをyに代入する

print('配列の要素の並びを反転したものをコピーしました。')
for i in range(len(y)):
    print(f'y[{i}] = {y[i]}')
