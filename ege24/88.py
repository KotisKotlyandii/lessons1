import sys

sys.stdin = open('24data/24-1.txt')

tekst = input()

chisla = ''
stolb = []
for i in range(len(tekst)-1):
    if tekst[i]  in "1234567890" and tekst[i+1] in "1234567890":
        if i+2 == len(tekst):
            chisla += tekst[i]
            chisla += tekst[i+1]
        else:
            chisla += tekst[i]
    elif tekst[i] in '1234567890' and tekst[i+1] not in '1234567890':
        chisla += tekst[i]
        if int(chisla[-1]) % 2 == 1:
            stolb.append(int(chisla))
            chisla = ''
        else:
            chisla = ''
    else:
        if len(chisla) != 0:
            if int(chisla[-1]) % 2 == 1:
                stolb.append(int(chisla))
                chisla = ''
            else:
                chisla = ''
if len(chisla) != 0:
    if int(chisla[-1]) % 2 == 1:
        stolb.append(int(chisla))
print(min(stolb))