def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

for n in range(4,37):
    if int('21',n) * int('13',n) == int('313',n):
        print(n)