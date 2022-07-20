def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

a = (2*343**123 + 2401) * (3*343**137 - 2401)
print(f(a,7).count(6))