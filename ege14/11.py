def f(c,n):
    s = []
    while c != 0:
       s.append(c%n)
       c //= n
    return s[::-1]
k = []
for c in range(1,18):
    if len(set(f(c,3)[-2:])) == 1:
        print(f(c,3))
        k.append(c)
print(k)

