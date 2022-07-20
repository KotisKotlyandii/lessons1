def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]
s = []
for x in range(1,10000):
    a = 7 ** 500 + 7 ** 200 - 7 ** 50 - x
    s.append(sum(f(a,7)))

print(max(s))