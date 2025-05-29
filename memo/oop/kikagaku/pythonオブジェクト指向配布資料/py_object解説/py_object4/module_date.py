import datetime

print(datetime.date.today())
print(datetime.datetime.now())

xmas_2021 = datetime.date(2021, 12, 25)
print(xmas_2021 - datetime.date.today())

a = datetime.date(2022, 6, 21)
print(a - datetime.date.today())
