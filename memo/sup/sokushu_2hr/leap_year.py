def is_leap_year(year: int):
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

print(f"1999 is a leap year -> {is_leap_year(1999)}")
print(f"2000 is a leap year -> {is_leap_year(2000)}")
print(f"2024 is a leap year -> {is_leap_year(2024)}")
print(f"2025 is a leap year -> {is_leap_year(2025)}")
