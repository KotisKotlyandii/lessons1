import  sys
sys.stdin = open("24data/k7b-1.txt")

s = input()
spis = []
dlina = 0
ne_prov = 0

for i in range(0,len(s)):
    if s[i] == "E" and s[i + 1] == "A" and s[i + 2] == "B":
        if ne_prov > 0 and ne_prov != 3:
            ne_prov += 1
        else:
            dlina += 3
            ne_prov = 0
    elif s[i] == "E" and s[i + 1] == "A":
        dlina += 2
    elif s[i] == "E":
        dlina += 1
    else:
        spis.append(dlina)
        dlina = 0


print(max(spis))