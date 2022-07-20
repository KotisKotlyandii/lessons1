def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]


a = 4 ** 503 + 3*4**244 - 2*4**444 - 95
print(f(a,4).count(3))