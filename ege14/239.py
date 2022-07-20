def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

a = (729 ** 41 - 81 ** 16) * (729 ** 15 + 9 ** 5)
print(f(a,9).count(8))