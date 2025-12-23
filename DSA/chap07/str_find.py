# 文字列に含まれる文字列を探索（find系メソッド）

txt = input('文字列txt：')
pat = input('文字列ptn：')

c = txt.count(pat)

if c == 0:                                              # 含まれない
    print('patはtxtに含まれません。')
elif c == 1:                                            # １個だけ含まれる
    print(f'patがtxtに含まれるインデックス：{txt.find(pat)}')
else:                                                   # ２個以上含まれる
    print(f'patがtxtに含まれる先頭インデックス：{txt.find(pat)}')
    print(f'patがtxtに含まれる末尾インデックス：{txt.rfind(pat)}')
