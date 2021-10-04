

def f(n):
    global s
    s += n+1
    if n > 1:
        s += 2*n
        f(n-1)
        f(n-3)
    return s


for n in range(1,1000):
    s = 0
    if f(n) > 1000000:
        print(n,f(n))
        break