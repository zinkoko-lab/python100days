# 文字列に含まれる文字列を探索（indexメソッド）

txt = input('文字列txt：')
pat = input('文字列pat：')

try:
    print(f'txt[{txt.index(pat)}]にpatが含まれます。')
except ValueError:
    print('patはtxtに含まれません。')
