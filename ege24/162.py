import  sys

sys.stdin = open('24data/24-s1.txt')

s = []
byk = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for _ in range(1000):
    s.append(input())
nomer = []
for i in s:
    kol = 0
    for n in range(len(i)-1):
        if i[n:n+2] in byk:
            kol += 1
    if kol == 0:
        nomer.append(10000)
    else:
        nomer.append(kol)
naim_stroka = s[nomer.index(min(nomer))]
slovarik = {}
for i in naim_stroka:
    slovarik[i] = naim_stroka.count(i)

slovarik = {n:slovarik[n] for n in slovarik if slovarik[n] != 0}
max_str = max(slovarik.values())

bykv = max([i for i in slovarik if slovarik[i] == max_str])
kol = sum([i.count(bykv) for i in s])
print(bykv, kol)