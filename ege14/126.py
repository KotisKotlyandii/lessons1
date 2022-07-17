def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

for c in range(1,1000):
    if f(c,16)[0] == 1 and f(c,16)[-1] == 0 and len(f(c,16)) == 3 and f(c,8)[0] == 5 and f(c,8)[1] == 6 and len(f(c,8)) == 3:
        print(c)