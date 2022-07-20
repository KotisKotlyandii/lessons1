def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

print(f(7 ** 500 + 7 ** 200 - 7 ** 50, 7))
print((len(f(7 ** 500 + 7 ** 200 - 7 ** 50, 7))-1)*6)
