def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]


a = 6*343**1156 - 5*49**1147 + 4*7**1153 - 875
print(sum(f(a,7)))