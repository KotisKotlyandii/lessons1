def F(n):
    if n < 1:
        return n
    elif n >= 1 and n % 2 == 0:
        return n + 3 * F(n-3)
    elif n >= 1 and n % 2 == 1:
        return 5*n + 2 * F(n-5)

print(F(30))