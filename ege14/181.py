def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

for n in range(7,37):
    if int('211',n) == int('152',n+1):
        print(n)