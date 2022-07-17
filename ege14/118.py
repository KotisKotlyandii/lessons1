def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

for n in range(5,100):
    if int('224',n) + 1 == int('101',8):
        print(n)