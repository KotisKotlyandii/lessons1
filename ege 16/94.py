def f(n):
    if n < 2:
        return  1
    if n % 3 == 0:
        return f(n//3) - 1
    else:
        return f(n-1) + 17


for n in range(1,100000):
    if f(n) == 110:
        print(n)
        break