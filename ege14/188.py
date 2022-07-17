def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

for n in range(7,34):
    if int('221',n) + int('34',8) == int('180',n+2):
        print(n)