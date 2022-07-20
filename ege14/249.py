def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

a = 5**2*7**25+6**2*7**36 - 4**2*9**3
print(f(a,7).count(0))