def f(a,b):
    if a == b:
        return 1
    elif a > b:
        return 0
    return f(a+2,b) + f(a+3,b) + f(a*10+1,b)

print(f(3,12)*f(12,25))