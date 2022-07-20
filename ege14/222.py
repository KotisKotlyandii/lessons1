def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

a = 4**3*3**19
print(f(a,3).count(0),f(a,3).count(1),f(a,3).count(2))