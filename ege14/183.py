def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

for n in range(8,34):
    if int('123',n) == int('93',n+2):
        print(n)