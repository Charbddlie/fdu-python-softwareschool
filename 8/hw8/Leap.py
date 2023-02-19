def isLeap(year):
    if year % 400 == 0 or (year % 4 == 0 and not year % 100 == 0):
        return True
    else:
        return False
