def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

a = 5**94 + 25 ** 49 - 130
print(f(a,5).count(4))