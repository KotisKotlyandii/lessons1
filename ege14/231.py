def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]
k = []
for x in range(2,120):
    for y in range(2,120):
        a = (55+2*5**x) * 5 ** x + 55 + 5 ** y
        k.append(sum(f(a,5)))

print(max(k))