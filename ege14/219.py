def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

for n in range(5,37):
    if int('13',n) * int('31',n) == int('423',n):
        print(n)