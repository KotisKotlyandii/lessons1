import sys
sys.stdin = open("24data/k7b-5.txt")

s = input()
spis = []
dlina = 0

for i in range(0,len(s),2):
    if s[i] == "C" and s[i + 1] == "A":
        dlina += 2
    elif s[i] == "C":
        dlina += 1
    else:
        spis.append(dlina)
        dlina = 0

print(max(spis))
