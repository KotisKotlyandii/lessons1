def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]
k = []
s = 0
for n in range(2,11):
    if len(set(f(1755,n))) == len(f(1755,n)):
        s += n

print(s)