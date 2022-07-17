def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

for n in range(5,100):
    if int('441',n) + 14 == 135:
        print(n)
        print(f(n,2))