import datetime as dt

now = dt.datetime.now()
year = now.year
print(f"year: {year}")
month = now.month
print(f"month: {month}")
day = now.day
print(f"day: {day}")
day_of_week = now.weekday()
print(f"day_of_week: {day_of_week}")

date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
print(date_of_birth)
