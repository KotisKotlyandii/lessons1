def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

for n in range(7,37):
    if int('214',n) == int('165',n+1):
        print(n)