def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]


a = 2*9**10 - 3**5 + 5
print(f(a,3).count(2))