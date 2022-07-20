def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]
k = []
s = 0
for n in range(2,11):
    if 2 not in f(652,n):
        s += n

print(s)