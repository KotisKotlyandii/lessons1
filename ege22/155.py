def f(x):
    K,P,S = x-1,100,340
    while P < S:
        K += 1
        S -= 2 * K
        P += K
    K -= x
    return K

for x in range(1,10000):
    if f(x) == 5:
        print(x)