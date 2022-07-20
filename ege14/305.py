def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]


a = 6**1333 - 5*6**1215 + 3*6**144 - 86
print(sum(f(a,6)))