def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

a = 32**2 + 1024 + 1024 ** 2
print(hex(a))
print(hex(a).count('0'))