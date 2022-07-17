def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

k = []
for n in range(2, 100):
    if f(63,n)[-2:] == [2,3]:
        k.append(n)
print(k)

