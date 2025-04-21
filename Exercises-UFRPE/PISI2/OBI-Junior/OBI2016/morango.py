def morango(x1, y1, x2, y2):
    if x1*y1 > x2*y2:
        return x1*y1
    else:
        return x2*y2

print(morango(12, 38, 5, 20))
