def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

a = 4**4*5**69-70
print(f(a,5).count(0),f(a,5).count(1),f(a,5).count(2),f(a,5).count(3),f(a,5).count(4))