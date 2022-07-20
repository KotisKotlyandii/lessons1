def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]
k = 0
for n in range(2,11):
    if sum(f(538,n)) % 2 == 0:
        k += n
print(k)