def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]


a = 4*125**4 - 25**4 + 9
print(f(a,5).count(4))