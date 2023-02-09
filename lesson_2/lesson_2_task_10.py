# def bank(x, y):
#     for y in range (0, y):
#         x = x+x*0.1
#     return x

# print(bank(5000, 5))

# Лучше с говорящими именами и округдение до 4х знаков
def calc_deposit(sum, term):
    for term in range (0, term):
        sum = sum*1.1
    return round(sum,4)

print(calc_deposit(5000, 5))
