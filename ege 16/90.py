def f(n):
    if n == 1:
        return n
    if n >= 2 and n % 2 == 0:
        return f(n//2) + 1
    else:
        return f(n-1) + n

for n in range(1,1000):
    if f(n) == 19:
        print(f(n))
        break