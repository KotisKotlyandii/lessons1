def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]
k = 0
for n in range(2,11):
    if f(123,n) == sorted(f(123,n)):
        k += n
print(k)