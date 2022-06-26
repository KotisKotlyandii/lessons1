def nahod(a,b):
    if a == b:
        return 1
    elif a > b:
        return 0
    return nahod(a+1, b) + nahod(a*4,b)

print(nahod(1,55))