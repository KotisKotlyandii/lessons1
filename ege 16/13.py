def F(n):
    if n < 3:
        return 2*n
    elif n >= 3 and n % 2 == 0:
        return 3*n + 5 + F(n-2)
    elif n >= 3 and n % 2 == 1:
        return n + 2 * F(n-6)

print(F(61))