for n in range(1,30):
    c = n
    while c > 4:
        c //= 5
    if c == 3:
        print(n)