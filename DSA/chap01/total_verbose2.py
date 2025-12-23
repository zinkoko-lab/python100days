# aからbまでの総和を求める（求める式も表示：その２）

print('aからbまでの総和を求めます。')
a = int(input('整数a：'))
b = int(input('整数b：'))

if a > b:
    a, b = b, a

total = 0
for i in range(a, b):
    print(f'{i} + ', end='')
    total += i      # totalにiを加える

print(f'{b} = ', end='')
total += b          # totalにbを加える

print(total)        # 総和
