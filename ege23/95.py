def f(a,b):
    if a == b:
        return 1
    elif a > b or a == 14:
        return 0
    return f(a+1,b) + f(a+3,b)

print(f(2,9)*f(9,18))