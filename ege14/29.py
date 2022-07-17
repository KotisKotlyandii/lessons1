def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]
k = []
for n in range(2,100):
    if f(35,n)[-1] == 8:
        k.append(n)
        print(f(35,n))
print(k)