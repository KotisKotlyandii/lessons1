def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

a = 16**21 + 4**36 - 8 ** 8 - 2 ** 64 + 31
print(f(a,16).count(15)+f(a,16).count(1))