def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

print(f(2,6))
print(f(7,7))
print(f(6,6))
print(f(10,6))