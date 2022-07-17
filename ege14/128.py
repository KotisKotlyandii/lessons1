def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

for c in range(20,1000):
    if f(c,2)[:2] == [1,0] and len(f(c,2)) == 8 and f(c,8)[1] == 4 and len(f(c,8)) == 3 and f(c,16)[-1] == 2 and len(f(c,16)) == 2:
        print(c)