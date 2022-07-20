def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

a = ((44 + 4 ** 50)*4**25 + 44) * 4 ** 12 + 44
print(f(a,4).count(0),f(a,4).count(1),f(a,4).count(2),f(a,4).count(3))