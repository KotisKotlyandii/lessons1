def f(x):
    P, S,K = 90, 6*(x-x%22),0
    while P < 181:
        K += 1
        P += K
        S -= 2*K
    return S


for x in range(1,100000):
    if f(x) == 82:
        print(x)