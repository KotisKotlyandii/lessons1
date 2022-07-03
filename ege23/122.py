def f(a,b):
    if a == b:
        return 1
    elif a > b:
        return 0
    return f(a+2,b) + f(a+4,b) + f(a+5,b)

k = 0
while f(31,k) != 1001: k += 1
print(k)