import sys


sys.stdin = open('24data/24-1.txt')

t = input()

spis_raz = []
m = max(t)
nachalo = t.index(m) + 1
t = t[:t.rfind(m)]
while True:
    if m in t[nachalo:]:
        perv = t[nachalo:].index(m) + nachalo
    else:
        break
    nachalo = t[nachalo:].index(m) + (len(t) - len(t[nachalo:]) + 1)
    if m in t[nachalo:]:
        vtor = t[nachalo:].index(m) + nachalo
        spis_raz.append(abs(perv - vtor))
    else:
        break

print(max(spis_raz))