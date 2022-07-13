def f(x):
    L = 2*x-20
    M = 2*x+30
    while L != M:
        if L > M:
            L -= M
        else:
            M -= L
    return M

for x in range(201,100000):
    if f(x) == 50:
        print(x)
        break