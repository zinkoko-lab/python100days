# 帰属性判定演算子による文字列が含まれるかどうかの判定

txt = input('テキスト：')    # テキスト用文字列
pat = input('パターン：')    # パターン用文字列

print(f'{pat in txt     = }')
print(f'{pat not in txt = }')
