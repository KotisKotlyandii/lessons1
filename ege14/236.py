def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

a = 8*345**5 + 9 * 49 ** 8 - 48
print(f(a,7).count(6))