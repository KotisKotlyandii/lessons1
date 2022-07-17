def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

for n in range(3,100):
    if int('121',n) + 1 == int('101',9):
        print(n)