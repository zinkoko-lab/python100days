# リストの文字列化と表示

x = [1, 2, 3]

print(' '.join(str(i) for i in x))          # 1 2 3

print()

print('  '.join(str(i) for i in x))         # 1  2  3
print(', '.join(str(i) for i in x))         # 1, 2, 3
print('\n'.join(str(i) for i in x))         # １行に１個ずつ表示

print()

x = [123, 4,  9999]
y = [32, 1357, 12, 77777]
print(''.join(f'{i:6}' for i in x))         #    123     4  9999
print(''.join(f'{i:6}' for i in y))         #     32  1357    12 77777

print()

a = [[11, 22, 3333], [4444, 55555], [666, 7777, 88]]
print('\n'.join(''.join(f'{a[i][j]:8}'          #       11      22    3333
                 for j in range(len(a[i])))     #     4444   55555
                 for i in range(len(a))))       #      666    7777      88
