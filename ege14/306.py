def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]


a = 4 ** 1503 + 3*4**244 - 2*4**1444 - 96
print(sum(f(a,4)))