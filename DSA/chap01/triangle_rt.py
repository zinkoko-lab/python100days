# 右上側が直角の二等辺三角形を表示

print('右上直角の二等辺三角形')
n = int(input('短辺の長さ：'))

for i in range(n):
    for _ in range(i):
        print(' ', end='')
    for _ in range(n - i):
        print('*', end='')
    print()
