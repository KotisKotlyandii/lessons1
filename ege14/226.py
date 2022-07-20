def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

a = (77+7**77)*7**77 + 77 + 7 ** 7
print(f(a,7).count(0),f(a,7).count(1),f(a,7).count(2),f(a,7).count(3),f(a,7).count(4),f(a,7).count(5),f(a,7).count(6))