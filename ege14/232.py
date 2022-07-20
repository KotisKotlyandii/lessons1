def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]
k = []
for x in range(2,160):
    for y in range(2,160):
        a = (3 + 2*4**x) * 4 ** x + 3 + 4 ** y
        k.append(sum(f(a,4)))
print(k)
print(max(k))