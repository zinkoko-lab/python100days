"""
書式 -> try文の例です

try:
    例外が発生する可能性がある処理
except:
    例外が発生した時の処理

"""

a = ["ten", "11", "12", "13"]
b = 0
for n in a:
    try:
        b += int(n)
    except ValueError:
        pass

print(f"b = {b}")
