import  sys

sys.stdin = open('24data/24-171.txt')

spis = []
for _ in range(9482):
    t = input()
    t = t.replace('XYZ', '_')
    spis.append(t)
k = 0
spisok = []
for t in spis:
    for i in t:
        if i == '_':
            k += 1
        else:
            spisok.append(k)
            k = 0

print(max(spisok))
print("Z"+18*"_"+"Y" in )