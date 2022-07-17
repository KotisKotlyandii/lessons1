def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]


for n in range(4, 100):
    if int('103',n) + 11 == int('103',n+1):
        print(n)