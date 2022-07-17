def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

for n in range(8,34):
    if int('143',n) + int('25',6) == int('138',n+1):
        print(n)