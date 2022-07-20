def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

a = 2 ** 102 + 2 ** 100 + 2 ** 85 + 2 ** 17
print(len(set(f(a,8))))