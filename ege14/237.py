def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

a = 7 * 1296 ** 57 - 8 * 216 ** 30 + 35
print(f(a,6).count(5))