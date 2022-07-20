def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

for x in range(2,10000):
    a = 64 ** 11 - 4 ** 10 + 96 - x
    if sum(f(a,4)) == 71:
        print(x)