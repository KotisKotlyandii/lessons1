import  sys

sys.stdin = open('24data/24-171.txt')

spis = []
for _ in range(9482):
    t = input()
    t = t.replace('XYZ', '_')
    spis.append(t)

bykv = 'ABCDEFGHIJKLMNOPQRSTUVW'

vtor = []
trei = []
for t in spis:
    for i in bykv:
        t = t.replace('%s' % i, ' ')
        trei = list(map(str,t.split()))
    for a in trei:
        if a[0] in "XYZ" and a[-1] in "XYZ" and ("X" not in a[1:-1] and "Y" not in a[1:-1] and "Z" not in a[1:-1]):
            vtor.append(len(a[1:-1])*3+2)
print(max(vtor))
