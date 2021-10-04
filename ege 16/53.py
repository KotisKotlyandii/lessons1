def f(n):
    if n > 15:
        return n*n-5
    else:
        return n*f(n+2)+n+f(n+3)

print(f(1))