def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

a = 256 ** 2 + 4096 ** 16 - 15
print(hex(a).count('f'))