def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]
k = []
s = 0
for n in range(2,11):
    if f(7667,n) == f(7667,n)[::-1]:
        s += n
print(s)
