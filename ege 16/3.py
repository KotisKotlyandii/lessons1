def F(n):
    if n == 1:
        return 2
    else:
        return F(n-1) +5 * n**n

print(F(39))