def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]


a = 7 ** 103 + 20*7**204 - 3*7**57 + 97
print(f(a,7).count(6))