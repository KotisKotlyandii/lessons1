for _ in range(int(input())):
    kol,h1,m1 = map(int,input().split())
    raz = []
    for _ in range(kol):
        h2,m2 = map(int,input().split())
        s = (24*60 - (h1*60+m1)) + (h2*60+m2) if h1-h2 > 0 or (h1==h2 and m1 - m2 > 0) else abs((h1*60+m1)-(h2*60+m2))
        raz.append(s)
    print(min(raz)//60,(min(raz)%60))