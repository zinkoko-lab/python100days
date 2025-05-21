def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

year = 2000
print(f"year{year} is a leap year? => {is_leap(year)}") # True

year = 2100
print(f"year{year} is a leap year? => {is_leap(year)}") # False

year = 2400
print(f"year{year} is a leap year? => {is_leap(year)}") # True

year = 1989
print(f"year{year} is a leap year? => {is_leap(year)}") # False

year = 2024
print(f"year{year} is a leap year? => {is_leap(year)}") # True
