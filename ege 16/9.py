def F(n):
    if n > 16:
        return n-3
    else:
        return 2 * F(n+1) + 2*n + 3

print(F(2))