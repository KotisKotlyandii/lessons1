def f(n):
    q = 0
    for i in range(1,n):
        if n % i == 0:
            q = i
    return q


for n in range(1,10000):
    if f(n) == 17:
        print(n)
