a = 2 ** 51 + 2 ** 40 + 2 ** 35 + 2 ** 17 - 2 ** 5
def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

print(len(set(f(a,16))))