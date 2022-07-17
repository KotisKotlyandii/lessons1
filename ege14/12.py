def f(c,n):
    s = []
    while c != 0:
       s.append(c%n)
       c //= n
    return s[::-1]
k = 0
for c in range(19,34):
    k += f(c,6).count(3)
print(k)