def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s


for c in range(1,10000):
    if f(c,8)[0] == 0 and f(c,9)[0] == 0:
        print(c)
        break