import sys

sys.stdin = open('24data/24-j2.txt')


t = input()
spis = []
prib = 1
for i in range(len(t)-1):
    if t[i] == t[i+1]:
        prib += 1
    else:
        if prib == 1:
            continue
        else:
            spis.append(prib)
            prib = 1

print(max(spis))