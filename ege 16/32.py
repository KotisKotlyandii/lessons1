def f(n):
    if n<10:
        return n
    else:
        m=f(n//10)
        d=m%10
        if m < d:
            return d
        else:
            return m

max = 0

for n in range(100,1500):
    if f(n) > 7:
        max = n


print(max,f(max))
