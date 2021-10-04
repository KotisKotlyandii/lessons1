def f(n):
    if n > 0:
        d = (n%10 + f(n//10))
        return  d
    else:
        return 0


for n in range(1,1000000):
    if f(n) > 51:
        print(n, f(n))
        break