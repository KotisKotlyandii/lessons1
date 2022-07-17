def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

for n in range(2,100):
    if f(41,n)[-1] == 8 and f(63,n)[-1] == 8:
        print(n)