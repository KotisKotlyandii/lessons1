def f(a,b):
    if a == b:
        return 1
    elif a > b or a == 8:
        return 0
    return f(a+1,b) + f(a+2,b) + f(a*2,b)

print(f(3,13))