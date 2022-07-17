def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

a = 25** 94 + 5 ** 216 - 125
print(f(a,5).count(4))