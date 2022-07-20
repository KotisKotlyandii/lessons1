def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

for x in range(2,10000):
    a = 64 ** 12 - 8 ** 14 + x
    if oct(a).count('7') == 12 and oct(a).count('1') == 1:
        print(x)