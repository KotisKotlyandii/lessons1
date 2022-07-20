def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

a = 5 * 6561 ** 46 + 5 * 729 ** 15 - 5 * 5832 - 5
print(f(a,9).count(4))