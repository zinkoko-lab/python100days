# aからbまでの総和を求める（求める式も表示：その１）

print('aからbまでの総和を求めます。')
a = int(input('整数a：'))
b = int(input('整数b：'))

if a > b:
    a, b = b, a

total = 0
for i in range(a, b + 1):
    if i < b:       # 途中
        print(f'{i} + ', end='')
    else:           # 最後
        print(f'{i} = ', end='')
    total += i      # totalにiを加える

print(total)        # 総和
