def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

a = 17 ** 5 + 85 ** 8 - 10
print(f(a,17).count(16))