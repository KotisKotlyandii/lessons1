def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

a = 7 ** 2 + 49 ** 4 - 21
print(f(a,14).count(10)+f(a,14).count(0))