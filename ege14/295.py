def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]


a = 6 ** 203 + 5*6**405 - 3*6**144 + 77
print(f(a,6).count(5))