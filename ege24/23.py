import  sys

sys.stdin = open("24data/k7a-3.txt")

tekst = input()
spis = []
tek = 0

for i in range(len(tekst)):
    if tekst[i] == "A" or tekst[i] == "B" or tekst[i] == "F" or tekst[i] == "E":
        tek += 1
    else:
        spis.append(tek)
        tek = 0

print(max(spis))