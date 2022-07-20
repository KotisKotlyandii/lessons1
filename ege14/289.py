def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

for x in range(2,10000):
    a = 81 ** 20 - 9 ** x + 50
    if sum(f(a,9)) == 138:
        print(x)