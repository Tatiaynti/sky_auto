def month_to_season(month):
    if month == 1 or month == 2 or month == 12:
        print ('Зима')
    elif 3 <= month <= 5:
        print ('Весна')
    elif 6 <= month <= 8:
        print ('Лето')
    elif 9 <= month <= 11:
        print ('Осень')

month_to_season(6)