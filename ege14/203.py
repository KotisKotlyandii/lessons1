def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

a = 81 ** 5 + 3 ** 30 - 27
print(f(a,9).count(8))