def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]
k = 0
for c in range(20,1000):
    if len(f(c,16)) == 3 and f(c,16)[::2] == [3,9] and len(f(c,8)) == 3 and f(c,8)[0] == 1:
        k += 1
print(k)