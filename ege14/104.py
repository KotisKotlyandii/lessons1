def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

for n in range(6,100):
    if int('145',n) + 24 == int('127',9):
        print(n)
        print(f(n,5))