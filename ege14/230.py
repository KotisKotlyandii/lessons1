def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

a = (88+2*8**4) * 8 ** 4 + 88 + 8 ** 8
print(sum(f(a,8)))