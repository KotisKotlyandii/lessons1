import  sys

sys.stdin = open('24data/24-2.txt')

tekst = input()
slovarik = []
posled = 1
for i in range(len(tekst)-1):
    if tekst[i] < tekst[i+1]:
        posled += 1
    else:
        slovarik.append(posled)
        posled = 1
slovarik.append(posled)
print(max(slovarik))