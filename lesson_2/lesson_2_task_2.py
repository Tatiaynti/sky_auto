def is_year_leap(year):
    if (year%4 == 0) :
        print("год " + str(year) + ": " + str(True))
    else:
        print("год " + str(year) + ": " + str(False))

is_year_leap(2024)