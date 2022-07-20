def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]


a = 4**103 + 3*4**444 - 2 *4**44 + 67
print(f(a,4).count(3))