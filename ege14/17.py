def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]


for n in range(2,100):
    if f(49,n) == [1,0,0]:
        print(n)
        