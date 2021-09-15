def is_leap(year):
    leap = False
    if year % 400 == 0:
        leap = True
    elif year % 4 == 0 and year % 100:
        leap = True
    return leap

y = int(input())
leap_year = is_leap(y)
print(leap_year)
