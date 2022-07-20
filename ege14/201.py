def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

a = 25 ** 56 + 5 ** 138 - 5
print(f(a,5).count(4))