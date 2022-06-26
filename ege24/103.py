import  sys

sys.stdin = open('24data/24.txt')


tekst = input()
max_p = ''
posled = tekst[0]
nachalo = 0
for i in range(len(tekst)-1):
    if tekst[i] < tekst[i+1]:
        posled += tekst[i+1]
        if len(posled) > len(max_p):
            max_p = posled
            nachalo = i - len(posled) + 3
    else:
        posled = tekst[i+1]
print(max_p)
print(nachalo)