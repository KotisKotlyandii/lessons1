def f(x):
    L,M = 0,0
    while x > 0:
        L += 1
        if x % 16 % 2 == 0:
            M += 1
        else:
            M -= 1
        x //= 16
    return L,M
kol = 0
for x in range(1,10000):
    if f(x) == (6,0):
        kol += 1
        
print(kol)