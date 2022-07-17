def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

for c in range(21,30):
    if f(c,3)[-2:] == [1,1]:
        print(c)