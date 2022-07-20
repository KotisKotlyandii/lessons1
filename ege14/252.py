def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

a = (2**345+8**65-4**130)*(8**123-2**89+4**45)
print(sum(f(a,8)))