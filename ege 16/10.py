def F(n):
    if n > 12:
        return 2*n-5
    else:
        return 2 * F(n+2) + n-4

print(F(1))