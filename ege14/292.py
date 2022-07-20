def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

for x in range(2,10000):
    a = 27 ** 7 - 3 ** 11 + 36 - x
    if sum(f(a,3)) == 22:
        print(x)