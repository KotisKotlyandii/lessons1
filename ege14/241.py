def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

x = []
for c in range(1,1000):
    if f(c,9).count(3) >= 1 and len(f(c,9)) == 3 and len(f(c*3,9)) == 3:
        x.append(c)

print(max(x) + min(x))