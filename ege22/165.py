def f(x):
    P,S,i = 0, 10*(x - x % 15), 2
    while i < 20:
        S -= 2*i
        P += i
        i += 2
    return S,P

for x in range(1,1000000):
    if f(x) == (270,90):
        print(x)