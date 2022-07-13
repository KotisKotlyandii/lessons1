def f(x,n):
    s = ''
    while x > 0:
        s += str(x % n)
        x //= n
    return s[::-1]

for n in range(2,100):
    if len(f(30,n)) == 4 and f(30,n)[-1] == '0':
        print(n)
