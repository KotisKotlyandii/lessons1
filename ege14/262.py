def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]
k = []
s = 0
for n in range(2,11):
    if f(432,n) == sorted(f(432,n),reverse=True):
        s += n

print(s)