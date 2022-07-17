def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]
k = []
for c in range(1,21):
    if f(c,3)[0] == 2:
        k.append(c)
print(k)

