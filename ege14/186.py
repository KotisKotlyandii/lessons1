def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

for n in range(7,34):
    if int('154',n) + int('35',9) == int('170',n+1):
        print(n)