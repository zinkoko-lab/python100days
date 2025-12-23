# 1からnまでの総和を求める（while文）
# ループ終了後の変数iの値を表示

print('1からnまでの総和を求めます。')
n = int(input('nの値：'))

total = 0
i = 1

while i <= n:   # iがn以下のあいだ繰り返す
    total += i    # totalにiを加える
    i += 1      # iに1を加える
print(f'1から{n}までの総和は{total}です。')
print(f'iの値は{i}です。')
