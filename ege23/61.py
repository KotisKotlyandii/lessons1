def f(a,b):
    if a == b:
        return 1
    elif a > b or a == 6:
        return 0
    return f(a+2,b) + f(a*3,b)

print(f(2,20)*f(20,40))