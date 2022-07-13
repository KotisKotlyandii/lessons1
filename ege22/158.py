def f(x):
    a = 1
    while x > 0:
        a *= x % 7
        x //= 7
    return a


for x in range(1,100000):
    if f(x) == 54:
        print(x)
        break