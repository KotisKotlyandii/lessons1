def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]


a = 27**4 - 9 ** 5 + 3 ** 8 - 25
print(f(a,3).count(2))