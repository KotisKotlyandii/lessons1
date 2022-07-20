def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]
k = []
s = 0
for n in range(2,11):
    if f(609,n)[0] % 2 != f(609,n)[-1] % 2:
        s += n

print(s)
