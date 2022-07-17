def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]


a = 9 ** 5 + 3 ** 25 - 20
print(a)
print(sum(f(a,3)))