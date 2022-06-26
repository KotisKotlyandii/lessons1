import  sys

sys.stdin = open('24data/24-164.txt')

s = []
for _ in range(1000):
    s.append(input())

maxp = 0
stroka = ''
for i in s:
    tek = 1
    max_tek = 0
    for n in range(len(i)-1):
        if i[n] == i[n+1]:
            tek += 1
        else:
            if max_tek < tek:
                max_tek,tek = tek,1
    if max_tek > maxp:
        maxp = max_tek
        stroka = i

slovarik = {}
for i in stroka:
    slovarik[i] = stroka.count(i)

slovarik = {n:slovarik[n] for n in slovarik if slovarik[n] != 0}

max_str = max(slovarik.values())

bykv = min([i for i in slovarik if slovarik[i] == max_str])
kol = sum([i.count(bykv) for i in s])
print(bykv, kol)
