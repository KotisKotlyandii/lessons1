def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

for n in range(5,100):
    if int('3',n) * int('213',n) == int('1043',n):
        print(n)