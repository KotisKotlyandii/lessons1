def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

for c in range(1,21):
    if f(c,5)[-1] == 3:
        print(c)