def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]


a = 9 ** 20 + 3 ** 60 - 125
print(a)
print(f(a,3).count(2))