def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

for n in range(7,37):
    if int('12',n) * int('33',n) == int('406',n):
        print(n)