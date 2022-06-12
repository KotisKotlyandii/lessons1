import sys

sys.stdin = open('24data/24-1.txt')

tekst = input()

chisla = ''
stolb = []
for i in range(len(tekst)-1):
    if tekst[i]  in "1234567890" and tekst[i+1] in "1234567890":
        if i+2 == len(tekst):
            chisla += tekst[i] if int(tekst[i]) % 2 == 0 else ''
            chisla += tekst[i+1] if int(tekst[i]) % 2 == 0 else ''
        else:
            chisla += tekst[i] if int(tekst[i]) % 2 == 0 else ''
    elif tekst[i] in '1234567890' and tekst[i+1] not in '1234567890':
        chisla += tekst[i] if int(tekst[i]) % 2 == 0 else ''
        stolb.append(chisla)
        chisla = ''
    else:
        if len(chisla) != 0:
            stolb.append(chisla)
            chisla = ''
if len(chisla) != 0:
    stolb.append(int(chisla))
print(max(stolb))