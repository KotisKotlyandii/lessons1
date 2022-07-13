def f(x):
    L,M = 1,0
    while x > 0:
        if M < L:
            M += 1
        else:
            L += M
        x //= 6
    return L,M


for x in range(1,100000):
    if f(x) == (4,2):
        print(x)
        