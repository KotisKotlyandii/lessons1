def f(a,b):
    if a == b:
        return 1
    elif a > b or a == 13 or a == 15:
        return 0
    return f(a+1,b) + f(a+2,b) + f(a*3,b)

print(f(5,11)*f(11,26))