def f(n):
    if n <= 3:
        return n
    if n > 3 and n % 2 == 0:
        return 2*n+f(n-1)
    else:
        return n*n+f(n-2)

