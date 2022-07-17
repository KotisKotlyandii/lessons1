def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

for n in range(2,100):
    if len(f(338,n)) == 3 and f(338,n)[-1] == 2:
        print(n)