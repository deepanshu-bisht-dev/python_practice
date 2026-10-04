# Valid date checker (uses leap year logic)
def is_leap(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def is_valid_date(d, m, y):
    if y < 1 or m < 1 or m > 12 or d < 1:
        return False
    days_in_month = [31, 29 if is_leap(y) else 28, 31, 30, 31, 30,
                     31, 31, 30, 31, 30, 31]
    return d <= days_in_month[m - 1]

print(is_valid_date(29, 2, 2024))  
print(is_valid_date(29, 2, 2023))
print(is_valid_date(31, 4, 2024))  