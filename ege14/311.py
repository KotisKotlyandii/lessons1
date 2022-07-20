def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

a = 81**18 - (81**8 - 1) * ((8+1)**8+1) / 8 - 8
print(f(a,3).count(1))