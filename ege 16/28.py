def f(n):
    global s
    s += 2*n+1
    if n>1:
        s+=3*n-8
        f(n-1)
        f(n-4)
    return s
s = 0


for n in range(1,1000):
    s = 0
    if f(n) > 5000000:
        print(n,f(n))
        break