def f(x):
    a = 1
    while x > 0:
        a *= x % 9
        x //= 9
    return a


for x in range(1,100000):
    if f(x) == 60:
        print(x)
        break