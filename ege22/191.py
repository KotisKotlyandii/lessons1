def f(x):
    x, a, b = (x - x % 8) * 10, 1, 0
    while x > 0:
        if x % 2 != 0:
            a *= x % 4
        else:
            b += x % 4
        x //= 8
    return a
kol = 0
for x in range(10,1,-1):
        spisok = list(str(x))
        print(*spisok)
        # b = sorted(list(map(int,*spisok)),reverse= True)
        # print(b)