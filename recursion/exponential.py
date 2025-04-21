def exponential(num, exp):
    if exp == 0:
        return 1    # 2 elevado a 0 é 1
    else:
        return num * exponential(num, exp-1)
    

print(exponential(2, 1))
