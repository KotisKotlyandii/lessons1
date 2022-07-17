def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

a = 49**13 + 7 ** 33 - 49
print(f(a,7).count(6))