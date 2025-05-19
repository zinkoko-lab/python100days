# •	グローバル変数がイミュータブルな型（例：int, str, floatなど）の場合
# 関数の中でその値を変えるには global 宣言が必要です。

count_1 = 0  # グローバル変数
count_2 = 1  # グローバル変数

def add():
    global count_1, count_2
    count_1 += 1
    count_2 += 2

add()

print(count_1)
print(count_2)

r'''
•	グローバル変数がミュータブルな型（例: dict, listなど）の場合
関数の中で中身を更新するのは global 宣言なしでOKです。
ただし、変数自体を他のオブジェクトに再代入するときは global が必要です。
'''

info = {"name": "ZinKoko", "age": 30}
print("before update_age()")
print(info)

def update_age():
    info["age"] = 31

update_age()

print("after update_age()")
print(info)

# ミュータブルだけど再代入はNG（globalが必要）
# info = {"name": "ZinKoko", "age": 30}
# def reset_info():
#     info = {}  # これはローカル変数として新しいinfoを定義してしまう

# 正しく再代入したいなら：
def reset_info():
    global info
    info = {}
