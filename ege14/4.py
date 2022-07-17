def f(c,n):
    s = []
    while c != 0:
       s.append(c%n)
       c //= n
    return s
k = []
for n in range(2,100):
    if f(29,n)[0] == 5:
        k.append(n)
print(k)