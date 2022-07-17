def f(c,n):
    s = []
    while c != 0:
       s.append(c%n)
       c //= n
    return s

for n in range(2,100):
    if f(12,n) == [0,1,1]:
        print(n)
        