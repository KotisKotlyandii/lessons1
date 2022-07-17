def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

k = 0
for c in range(13,24):
    k += f(c, 4).count(3)

print(k)

