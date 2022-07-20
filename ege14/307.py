def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]


a = 7**1003 + 6*7**1104 - 3*7**57 + 294
print(sum(f(a,7)))