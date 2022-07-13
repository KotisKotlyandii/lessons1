def f(x):
    A,B = 0,1
    while x > 0:
        if x % 7 > 2:
            A += 1
        else:
            B *= x % 7
        x //= 7
    return A,B

for x in range(1,100000):
    if f(x) == (3,4):
        print(x)
        break