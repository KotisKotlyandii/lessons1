def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]


for n in range(2, 100):
    if int('101',n) + 13 == int('101',n+1):
        print(n)