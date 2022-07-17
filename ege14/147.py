def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]


a = 49 ** 12 - 7 ** 10 + 7 ** 8 - 49
print(f(a,7).count(6))