def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

for n in range(8,34):
    if int('103',n) == int('97',n+2):
        print(n)