def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]


a = 5*36**7 + 6 ** 10 - 36
print(f(a,6).count(5))