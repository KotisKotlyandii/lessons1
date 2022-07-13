def f(x):
    P,S,K = x,10*x,0
    while P < S:
        K += 1
        S -= 2 * K
        P += K
    return K

for x in range(1,100000):
    if f(x) == 10:
        print(x)
        break