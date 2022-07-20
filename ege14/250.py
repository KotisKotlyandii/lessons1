def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

a = 5**2004 - 5 **1016 - 25 ** 508 - 5 ** 400 + 25**250 - 27
print(f(a,5).count(4))