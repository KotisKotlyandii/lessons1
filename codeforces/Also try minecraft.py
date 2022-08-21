kol_stolb, test = map(int,input().split())
mas = list(map(int,input().split()))

for _ in range(test):
    nac,kon = map(int,input().split())
    nac -= 1
    itog = 0
    if nac > kon:
        for n in range(nac,kon-1,-1):
            itog += mas[n] - mas[n-1] if mas[n] > mas[n-1] else 0
    else:
        for n in range(nac,kon-1):
            itog += mas[n] - mas[n+1] if mas[n] > mas[n+1] else 0
    print(itog)
