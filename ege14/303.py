def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]


a = 4 ** 1103 + 3*4**1444 - 2*4**144 + 66
print(sum(f(a,4)))