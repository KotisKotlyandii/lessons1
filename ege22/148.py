def f(x):
    L = 3*x - 6
    M = 3*x + 99
    while L != M:
        if L > M:
            L -= M
        else:
            M -= L
    return M

for x in range(101,10000):
    if f(x) == 21:
        print(x)
        break