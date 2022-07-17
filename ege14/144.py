def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]


for n in range(5, 100):
    if int('104',n) + int('20',n) == 84:
        print(bin(n))