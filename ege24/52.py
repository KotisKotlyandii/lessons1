import  sys

sys.stdin = open('24data/k8-0.txt')

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
print(spisok)

