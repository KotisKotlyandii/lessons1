def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]
k = 0
for n in range(2,11):
    print(sum(f(437,n)))
    print(n)