def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]


a = 9 ** 9 + 3 ** 21 - 7
print(a)
print(f(a,3).count(0))