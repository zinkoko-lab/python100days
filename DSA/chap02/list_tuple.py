# リストとタプルの生成

list01 = []                   # []
list02 = [1, 2, 3]            # [1, 2, 3]
list03 = ['A', 'B', 'C',]     # ['A', 'B', 'C']

list04 = list()               # []              空リスト
list05 = list('ABC')          # ['A', 'B', 'C'] 文字列の個々の文字から生成
list06 = list([1, 2, 3])      # [1, 2, 3]       リストから生成
list07 = list((1, 2, 3))      # [1, 2, 3]       タプルから生成
list08 = list({1, 2, 3})      # [1, 2, 3]       集合から生成

list09 = list(range(7))           # [0, 1, 2, 3, 4, 5, 6]
list10 = list(range(3, 8))        # [3, 4, 5, 6, 7]
list11 = list(range(3, 13, 2))    # [3, 5, 7, 9, 11]

# 要素数が5で全要素が空のリストの生成
list12 = [None] * 5               # [None, None, None, None, None]

tuple01 = ()                    # ()
tuple02 = 1,                    # (1)
tuple03 = (1,)                  # (1)
tuple04 = 1, 2, 3               # (1, 2, 3)
tuple05 = 1, 2, 3,              # (1, 2, 3)
tuple06 = (1, 2, 3)             # (1, 2, 3)
tuple07 = (1, 2, 3,)            # (1, 2, 3)
tuple08 = 'A', 'B', 'C',        # ('A', 'B', 'C')

# 以下の二つは単一の値であってタプルではない
v01 = 1                         # 1   ※単一のintであってタプルではない
v02 = (1)                       # 1   ※単一のintであってタプルではない

tuple09 = tuple()           # ()              空タプル
tuple10 = tuple('ABC')      # ('A', 'B', 'C') 文字列の個々の文字から生成
tuple11 = tuple([1, 2, 3])  # (1, 2, 3)       リストから生成
tuple12 = tuple({1, 2, 3})  # (1, 2, 3)       集合から生成

tuple13 = tuple(range(7))           # (0, 1, 2, 3, 4, 5, 6)
tuple14 = tuple(range(3, 8))        # (3, 4, 5, 6, 7)
tuple15 = tuple(range(3, 13, 2))    # (3, 5, 7, 9, 11)

print(f'{list01 = }')
print(f'{list02 = }')
print(f'{list03 = }')
print(f'{list04 = }')
print(f'{list05 = }')
print(f'{list06 = }')
print(f'{list07 = }')
print(f'{list08 = }')
print(f'{list09 = }')
print(f'{list10 = }')
print(f'{list11 = }')
print(f'{list12 = }')

print(f'{tuple01 = }')
print(f'{tuple02 = }')
print(f'{tuple03 = }')
print(f'{tuple04 = }')
print(f'{tuple05 = }')
print(f'{tuple06 = }')
print(f'{tuple07 = }')
print(f'{tuple08 = }')
print(f'{v01 = }')
print(f'{v02 = }')
print(f'{tuple09 = }')
print(f'{tuple10 = }')
print(f'{tuple11 = }')
print(f'{tuple12 = }')
print(f'{tuple13 = }')
print(f'{tuple14 = }')
print(f'{tuple15 = }')
