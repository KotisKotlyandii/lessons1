def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

for c in range(20,1000):
    if f(c,16)[1] == 7 and len(f(c,16)) == 3 and f(c,8)[0] == 5 and f(c,8)[-1] == 6 and len(f(c,8)) == 3 and f(c,4)[-2] == 1 and len(f(c,4)) == 5:
        print(c)