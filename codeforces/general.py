def naxosh_min(min_rost):
    naxoh = 0
    for sol in range(len(spisok)):
        if spisok[sol] == min_rost:
            naxoh = sol
    return  naxoh
kol_soldat = int(input())
spisok = list(map(int,input().split()))
maks_rost, min_rost = max(spisok), min(spisok)
polos_max = spisok.index(maks_rost)
polos_min = naxosh_min(min_rost)
kol_second = 0
while True:
    while spisok[0] != maks_rost:
        if polos_max-1 == polos_min:
            spisok[polos_max], spisok[polos_max - 1] = spisok[polos_max - 1], spisok[polos_max]
            polos_max -= 1
            polos_min += 1
            kol_second += 1
        else:
            spisok[polos_max], spisok[polos_max-1] = spisok[polos_max-1], spisok[polos_max]
            polos_max -= 1
            kol_second += 1
    while spisok[-1] != min_rost:
        if polos_min + 1 == polos_max:
            spisok[polos_min], spisok[polos_min + 1] = spisok[polos_min + 1], spisok[polos_min]
            polos_min += 1
            polos_max -= 1
            kol_second += 1
        else:
            spisok[polos_min], spisok[polos_min+1] = spisok[polos_min+1], spisok[polos_min]
            polos_min += 1
            kol_second += 1
    break

print(kol_second)

