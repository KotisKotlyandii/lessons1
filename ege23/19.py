def f(a,b):
    if a == b:
        return 1
    elif a > b:
        return 0
    return f(a+1,b) + f(((a//10+1) * 10) + (a % 10),b)

print(f(11,27))