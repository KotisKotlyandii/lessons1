def f(c,n):
    s = []
    while c != 0:
       s.append(c%n)
       c //= n
    return s[::-1]
k = []
for c in range(1,31):
    if f(c,4)[-2:] == [3,1]:
        k.append(c)
print(k)

