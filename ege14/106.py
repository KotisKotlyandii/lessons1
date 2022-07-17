def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

for n in range(6,100):
    if int('33',n+4) - int('33',4) == 33:
        print(n)
        print(f(n,5))