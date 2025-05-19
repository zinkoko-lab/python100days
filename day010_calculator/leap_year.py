def is_leap_year(year):
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

year_1900 = is_leap_year(1900)
print(f"The year 1900 is {year_1900} year.")

year_2000 = is_leap_year(2000)
print(f"The year 2000 is {year_2000} year.")

year_2100 = is_leap_year(2100)
print(f"The year 2100 is {year_2100} year.")

year_2400 = is_leap_year(2400)
print(f"The year 2400 is {year_2400} year.")

year_1989 = is_leap_year(1989)
print(f"The year 2100 is {year_1989} year.")
