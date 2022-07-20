def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]
k = []
s = []
for n in range(2,11):
    k.append(f(572,n))
    s.append(n)
    print(n, k[-1])
