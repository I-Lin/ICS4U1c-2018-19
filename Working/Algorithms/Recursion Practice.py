def rpow(x, y):
    if y == 0:
        return 1
    else:
        return x * rpow(x, y-1)


print(rpow(2, 5))
