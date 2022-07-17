def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]


for n in range(2,37):
    if f(87,n)[-1] == 2 and 0 < len(f(87,n)) <= 3:
        print(n)