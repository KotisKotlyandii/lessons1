def f(a,b):
    if a == b:
        return 1
    elif a > b:
        return 0
    return f(a+1,b) + f(a+2,b)

print(f(4,12) + f(4,11))
