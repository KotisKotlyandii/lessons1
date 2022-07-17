def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]


a = 9 ** 14 + 3 ** 18 - 9 ** 5 - 27
print(a)
print(f(a,3).count(2))