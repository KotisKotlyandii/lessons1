def f(x):
    a,b,i,c = 0,0,0,0
    while x > 0:
        i += 1
        if i % 2 == 0:
            a += c
        else:
            b += c
        c = x % 10
        x //= 10
    return a,b

for x in range(1,100000):
    if f(x) == (3,2):
        print(x)
        break