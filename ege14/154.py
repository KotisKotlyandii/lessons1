def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]


a = 4*25**4 - 5**4 + 14
print(f(a,5))
print(sum(f(a,5)))