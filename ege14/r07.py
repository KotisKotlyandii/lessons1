for n in range(2,100):
    c = 30
    kol = 0
    while c > 0:
        c //= n
        kol += 1
    if kol == 3:
        print(n)
        break