a = 7 ** 202 + 49 ** 102 - 7 ** 20
def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]
print(f(a,7).count(6))