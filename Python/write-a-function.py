def is_leap(year):
    leap = False

    if year % 400 is 0:
        leap = True
    elif year % 100 is 0:
        leap = False
    elif year % 4 is 0:
        leap = True

    return leap