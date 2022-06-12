import sys

sys.stdin = open('24data/k8-7.txt')

tekst = input()
dlina = 2
stroki = []
for i in range(1,len(tekst)-1):
    if tekst[i] != tekst[i-1] and tekst[i] != tekst[i+1]:
        dlina += 1
    else:
        if dlina == 2:
            continue
        else:
            stroki.append(dlina)
            dlina = 2
stroki.append(dlina)
print(max(stroki))