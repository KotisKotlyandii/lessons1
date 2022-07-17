def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

a = 36 ** 17 + 6 ** 66 - 216
print(f(a,6).count(5))