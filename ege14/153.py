def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]


a = 2*27**7 + 3 ** 10 - 9
print(f(a,3).count(0))