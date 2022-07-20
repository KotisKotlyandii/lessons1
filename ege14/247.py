def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

for n in range(2,37):
    if sum(f(n**25 - 2*n**13 + 10,n)) == 75:
        print(n)