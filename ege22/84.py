def f(x):
    a,b,i = 0,0,0
    while x > 0:
        i += 1
        c = x % 10
        if i % 2 == 0:
            a += c
        else:
            b += c
        x //= 10
    return a,b

for x in range(1,100000):
    if f(x) == (3,2):
        print(x)
        break