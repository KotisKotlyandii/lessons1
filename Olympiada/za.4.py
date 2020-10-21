a = int(input())
xod = 0
kol_chifr = 0
for i in range(3**a):
    for _ in range(a):
        if i % 3 == 0:
            i = i // 3
        else:
            i -= 1
    if i == 1:
        kol_chifr += 1
print(kol_chifr+1)