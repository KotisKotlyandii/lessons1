def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

for n in range(7,34):
    if int('164',n) + int('41',9) == int('145',n+2):
        print(n)