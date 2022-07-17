def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]
k = []
for n in range(2,100):
    if f(144,n) == [2,6,4]:
        k.append(n)
        print(f(144,n))

print(k)