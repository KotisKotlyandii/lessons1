def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

for n in range(2,100):
    if f(68,n)[-1] == 3 and f(94,n)[-1] == 3:
        print(n)