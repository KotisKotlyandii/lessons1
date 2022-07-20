def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

a = 51*7**12 - 7 ** 3 - 22
print(sum(f(a,7)))