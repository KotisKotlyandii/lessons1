s = 0

def f(n):
    global s
    s += n+1
    if n > 1:
        s += n+5
        f(n-1)
        f(n-2)
    return s

for n in range(1,1000):
    s = 0
    if f(n) > 1000000:
        print(n,f(n))
        break