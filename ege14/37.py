def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

for n in range(5,100):
    if int('14',n) + int('42',n) == int('100',6):
        print(n)