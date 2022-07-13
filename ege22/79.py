def f(x):
    L = x - 15
    M = x + 20
    while L != M:
        if L > M:
            L -= M
        else:
            M -= L
    return M

for x in range(101,10000):
    if f(x) == 35:
        print(x)
        break