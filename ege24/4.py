import  sys

sys.stdin = open("24data/k7-20.txt")

tekst = input()
spis = []
tek = 0

for i in range(len(tekst)):
    if tekst[i] == "C":
        tek += 1
    else:
        spis.append(tek)
        tek = 0

print(max(spis))