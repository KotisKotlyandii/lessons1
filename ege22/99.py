def f(x):
    Q,L =6,0
    while x >= Q:
        L += 1
        x -= Q
    M = x
    if M < L:
        M = L
        L = x
    return L,M

for x in range(1,100000):
    if f(x) == (3,5):
        print(x)