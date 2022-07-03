def f(a,b):
    if a == b:
        return 1
    elif a > b or a == 18:
        return 0
    return f(a+1,b) + f(a+3,b)

print(f(3,12)*f(12,21))