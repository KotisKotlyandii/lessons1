def f(n):
    if n == 0:
        return 3
    if 0 < n <= 15:
        return f(n-1)
    if 15 < n < 95:
        return 2.5*f(n-3)
    else:
        return 3.3*f(n-2)

print(int(f(70)))