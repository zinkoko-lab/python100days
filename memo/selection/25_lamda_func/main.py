func = lambda x, y: print(f"{x}さんは{y}です。")
func("鈴木", "学生")

names = ["鈴木", "斉藤", "田中"]
result = list(map(lambda x: x + "さん", names))
print(result)

n1 = ["鈴木", "斉藤", "田中"]
n2 = ["めい", "ゆづき", "ひなた"]
result = list(map(lambda x, y: x + y + "さん", n1, n2))
print(result)

numbers = [1, 4, 6, 10, 22, 30]
result = list(filter(lambda x: x >= 10, numbers))
print(result)
