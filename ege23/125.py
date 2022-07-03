

def f(a,b):
    if a == b:
        return 1
    elif a > b or a == 33:
        return 0
    p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    c = [i for i in p if i > a][0]
    return f(a+2,b) + f(c, b)

print(f(2,14)*f(14,45))