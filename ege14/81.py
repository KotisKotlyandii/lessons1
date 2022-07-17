def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

for n in range(1,1000):
    if len(f(n,7)) == 2 and len(f(n,6)) == 3 and f(n,13)[-1] == 3:
        print(n)