def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

a = (512 ** 78 - 512 ** 60 ) * (512 ** 5 + 64 ** 5)
print(f(a,8).count(7))