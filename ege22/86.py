def f(x):
    b,i = 0,0
    while x > 0:
        b += x % 10
        x //= 10
        i += 1
    return i,b

for x in range(1,100000):
    if f(x) == (4,5):
        print(x)
        break