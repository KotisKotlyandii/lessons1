def f(a,b):
    if a == b:
        return 1
    elif a > b:
        return 0
    if a % 2 == 0:
        return f(a+1,b) + f(a*1.5,b)
    elif a % 2 == 1:
        return f(a+1,b)


print(f(1,20))