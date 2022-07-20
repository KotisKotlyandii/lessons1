def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]


a = 5*216**1256 - 5*36**1146 + 4*6**1053 - 1087
print(sum(f(a,6)))