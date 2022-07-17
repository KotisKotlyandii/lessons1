def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]


a = 3*16**8-4**5+3
print(f(a,4).count(3))