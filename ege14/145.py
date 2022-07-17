def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]


for x in range(9, 37):
    for y in range(8,37):
        if int('87',x) == int('73',y) and int('62',x) == int('52',y):
            print(x,y)