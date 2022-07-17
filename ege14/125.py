def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

for c in range(1,1000):
    if (f(c,16)[0] == 14 and len(f(c,16)) == 2) and (f(c,8)[1] == 5 and len(f(c,8)) == 3) and (f(c,4)[-1] == 1 and len(f(c,4)) == 4) and (f(c,2)[-3] == 1 and len(f(c,2)) == 8):
        print(c)