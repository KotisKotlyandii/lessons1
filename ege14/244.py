def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

a = ((7**(9**2-1) - (10-3)**4) * 5) // 6 * 8
print(f(a,7).count(4))