def F(n):
    if n < 0:
        return -1*n
    elif n >= 0 and n % 2 == 0:
        return 2*n + 1 + F(n-3)
    elif n >= 0 and n % 2 == 1:
        return 4*n + 2 * F(n-4)

print(F(33))