# 配列の要素の最大値を表示する（エラー）
# maxを変数として利用するため組込み関数maxが利用できなくなる

print('配列の最大値を求めます。')
num = int(input('要素数：'))
a = [None] * num  # 要素数numのリストを生成

for i in range(num):
    a[i] = int(input(f'a[{i}]：'))

max = a[0]
for i in range(1, len(a)):
    if a[i] > max:
        max = a[i]

print(f'最大値は{max}です。')
print(f'最大値は{max(a)}です。')        # エラー
