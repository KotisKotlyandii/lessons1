def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

a = 81 ** 2017 + 9 ** 5223 - 81
print(f(a,9).count(8))