def f(a,b):
    if a == b:
        return 1
    elif a > b:
        return 0
    return f(a+1,b) + f(a+2,b) + f(a*3,b)

print(f(2,4)*f(4,11)*f(11,15))