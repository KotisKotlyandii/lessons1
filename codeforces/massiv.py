for _ in range(int(input())):
    dlina, kol_zamen = map(int,input().split())
    perv = list(map(int,input().split()))
    vtor = list(map(int,input().split()))
    vtor.sort(reverse=True)
    if len(vtor) > kol_zamen:
        perv += vtor[0:kol_zamen]
    else:
        perv += vtor
    perv.sort(reverse=True)
    print(sum(perv[0:dlina]))
