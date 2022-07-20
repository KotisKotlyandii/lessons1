def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

a = 7 * 6561 ** 46 + 8 * 729 ** 15 - 6 * 5832
print(f(a,9).count(7))