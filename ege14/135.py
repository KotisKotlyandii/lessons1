def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]
k = 0
for c in range(20,1000):
    if f(c,16)[-1] == 10 and len(f(c,16)) == 2 and len(f(c,8)) == 3:
        k += 1
print(k)