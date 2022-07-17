def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

for n in range(6,34):
    if int('115',n) == int('57',n+2):
        print(n)