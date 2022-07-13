def f(x):
    M = 0
    for i in range(6):
        if x % 2 == 0:
            M += 1
        x //= 16
    return M
kol = 0

for x in range(16**5,16**6):
    if f(x) == 3:
        kol += 1
        
print(kol)