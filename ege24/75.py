import  sys

sys.stdin = open('24data/k8-12.txt')

tekst = input()

sim = ''
raaz = 1
spisok = []
for i in range(len(tekst)-1):
    if tekst[i] == tekst[i+1]:
        sim = tekst[i]
        raaz += 1
    else:
        if raaz == 1:
            continue
        else:
            spisok.append(str(str(raaz)+"_"+sim))
            sim = ''
            raaz = 1

maxim = "0_"
for i in range(len(spisok)):
    if int(spisok[i][0:spisok[i].index("_")]) > int(maxim[0:maxim.index('_')]):
        maxim = spisok[i]
spisokchek = []
spisokchek.append(maxim)

for i in range(len(spisok)):
    if int(spisok[i][0:spisok[i].index("_")]) == int(maxim[0:maxim.index('_')]):
        spisokchek.append(spisok[i])

print(maxim)
print(set(spisokchek))