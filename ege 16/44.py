def f(n):
    if n <= 3:
        return n
    if n > 3 and n % 3 == 0:
        return n*n*n + f(n-1)
    if n > 3 and n % 3 == 2:
        n*n + f(n-2)

print(100)