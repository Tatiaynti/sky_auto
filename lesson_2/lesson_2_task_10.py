def bank(x, y):
    for i in range (0, y):
        x = x+x*0.1
        i=i+1
    return x

print(bank(5000, 5))
