def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]
k = []
for c in range(1,1000):
    if f(c,5) == [1,2,3,4]:
        k.append(c)
print(k)
