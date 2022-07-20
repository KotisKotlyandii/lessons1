def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

a = 3**3*7**69-70
print(f(a,7).count(0),f(a,7).count(1),f(a,7).count(2),f(a,7).count(3),f(a,7).count(4),f(a,7).count(5),f(a,7).count(6))