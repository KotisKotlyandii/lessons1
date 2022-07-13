def f(x):
    Q,L =16,0
    while x >= Q:
        L += 1
        x -= Q
    M = x
    if M < L:
        M = L
        L = x
    return L,M

for x in range(1,100000):
    if f(x) == (8,11):
        print(x)