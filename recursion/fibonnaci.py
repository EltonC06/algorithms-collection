def fibonacci(num):
    if num == 1:
        return 1
    elif num == 2:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)
    


for n in range(1, 10):
    print(fibonacci(n))