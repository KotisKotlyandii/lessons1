def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]
k = []
for c in range(1,26):
    if f(c,2)[-3:] == [1,0,1]:
        k.append(c)
        print(f(c,2))
print(k)