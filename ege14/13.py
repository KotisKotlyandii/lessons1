def f(c,n):
    s = []
    while c != 0:
       s.append(c%n)
       c //= n
    return s[::-1]
k = 0
for c in range(12,32):
    k += f(c,5).count(1)
print(k)