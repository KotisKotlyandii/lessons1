def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

for n in range(3,100):
    if int('222',n) + 4 == 150:
        print(f(n,3))