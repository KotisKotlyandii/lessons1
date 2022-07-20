def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

a = (66 + 6 ** 2019) * 6 ** 2019 + 66 + 6**6
print(sum(f(a,6)))