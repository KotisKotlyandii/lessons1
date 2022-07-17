def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

for c in range(20,1000):
    if len(f(c,16)) == 3 and len(f(c,8)) == 3 and f(c,8)[::2] == [4,2]:
        print(c)