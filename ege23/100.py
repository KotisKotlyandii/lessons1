def f(a,b):
    if a == b:
        return 1
    elif a > b or a == 21:
        return 0
    return f(a+1,b) + f(a*3,b) + f(a*4,b)

print(f(2,16)*f(16,60))