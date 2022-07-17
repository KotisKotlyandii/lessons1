def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]


for n in range(2,100):
    if f(79,n)[-1] == 2 and f(111,n)[-1] == 1:
        print(n)