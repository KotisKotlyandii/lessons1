def f(n):
    if n > 0:
        return n%10*f(n//10)
    else:
        return 1

for n in range(1,1000):
    if f(n) > 320:
        print(n,f(n))
        break