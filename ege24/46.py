import  sys

sys.stdin = open('24data/k7-m21.txt')

tekst = input()
kol = 0
index = 0
print(tekst)
for i in range(len(tekst)-2):
    kol, index = (kol+1, i)  if tekst[i] < tekst[i+1] < tekst[i+2] else (kol, index)
print(kol,index)