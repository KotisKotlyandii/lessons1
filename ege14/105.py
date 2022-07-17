def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

for n in range(6,100):
    if int('44',n+5) - int('44',5) == 52:
        print(n)
        print(f(n,5))