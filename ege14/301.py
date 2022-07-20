def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]


a = 7 ** 103 + 6*7**104 - 3*7**57 + 98
print(sum(f(a,7)))