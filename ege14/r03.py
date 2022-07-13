def f(x,n):
    s = ''
    while x > 0:
        s += str(x % n)
        x //= n
    return s[::-1]


for n in range(2,100):
    if f(94,n)[:2] == '23':
        print(n)
