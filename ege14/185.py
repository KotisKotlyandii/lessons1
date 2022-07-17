def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

for n in range(4,34):
    if int('132',n) + int('13',8) == int('124',n+1):
        print(n)