def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]


a = 6**333 - 5*6**215 +3*6**144 - 85
print(f(a,6).count(5))