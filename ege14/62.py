def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

for c in range(1,1000):
    if f(c,4)[-1] == 0 and f(c,6)[-1] == 0:
        print(c)