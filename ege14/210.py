def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

a = 36 ** 10 + 6 ** 25 - 15
print(f(a,6).count(0))