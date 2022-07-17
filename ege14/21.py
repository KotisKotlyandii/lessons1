def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]
k = []
for c in range(1,26):
    if f(c,6)[0] == 4:
        k.append(c)
print(k)

