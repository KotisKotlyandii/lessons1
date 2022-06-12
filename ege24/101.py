import  sys

sys.stdin = open('24data/24-3.txt')


tekst = input()
slovarik = ''
posled = ''
for i in range(len(tekst)-1):
    if tekst[i] < tekst[i+1]:
        posled += tekst[i]
    elif tekst[i] != tekst[i+1] and tekst[i] > tekst[i+1]:
        posled += tekst[i]
        if len(posled) > len(slovarik):
            slovarik = posled
            posled = ''
        else:
            posled = ''
slovarik += tekst[-1]
print(slovarik)