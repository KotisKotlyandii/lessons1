import sys
sys.stdin = open('24data/24-168.txt')

t = input()
pa, pb, pc = t[0], t[1], t[2]
k1,k2,k3 = 1,1,1
spisok = []
for i in range(3,len(t)):
    if pc == t[i]:
        k3 += 1
    else:
        k1, pa = k2, pb
        k2, pb = k3, pc
        k3, pc = 1, t[i]
    if pa < pb < pc:
        spisok.append(k1+k2+k3)

print(max(spisok))