# ソートずみ配列のマージ（list関数とsorted関数を組み合わせる）

a = [2, 4, 6, 8, 11, 13]
b = [1, 2, 3, 4, 9, 16, 21]
c = [None] * (len(a) + len(b))

print('二つのソートずみ配列のマージ')

c = list(sorted(a + b))     # aとbを連結してソートしたものをlistに変換

print('配列aとbをマージして配列cに格納しました。')
print(f'配列a：{a}')
print(f'配列b：{b}')
print(f'配列c：{c}')
