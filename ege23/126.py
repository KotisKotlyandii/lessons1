def f(a,b):
    if a == b:
        return 1
    elif a > b:
        return 0
    return f(a+3,b) + f(a*2,b)

print(f(12,96))