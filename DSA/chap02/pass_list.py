# リストの任意の要素の値を更新する

def change(lst: list, idx: int, val: int) -> None:
    """lst[idx]の値をvalに更新"""
    lst[idx] = val

x = [11, 22, 33, 44, 55]
print(f'{x = }')

index = int(input('要素の添字：'))
value = int(input('新しい値　：'))

change(x, index, value)
print(f'{x = }')
