def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

for n in range(5,100):
    if int('144',n) + int('24',n) == int('201',n):
        print(n)