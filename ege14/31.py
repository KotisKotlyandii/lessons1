def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]
k = []
for c in range(1,16):
    if f(c,3)[-2:] == [2,1]:
        k.append(c)
print(k)
