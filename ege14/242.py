def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

a = 3*16**38 + 5*4**64 - 8**12 - 2**64 + 15
print(f(a,16).count(15))