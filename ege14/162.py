def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]


a = 9 ** 8 + 3 ** 24 - 6
print(a)
print(f(a,3).count(2))