def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]
k = []
for c in range(1,10000):
    if c % 16 == 0:
        k.append(f(c,2).count(0))
print(min(k))