def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

a = 36 ** 11 + 6 ** 25 - 21
print(f(a,6).count(5))