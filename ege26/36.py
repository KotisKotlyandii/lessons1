import sys

sys.stdin = open('26data/26-j8.txt')

k = int(input())
tov = []
for _ in range(k):
    tov.append(int(input()))


def perv(m):
    global k
    stariu = m.copy()
    noviy = []
    for _ in range(int(k*0.7)):
        noviy.append(min(stariu)*0.7)
        stariu.remove(min(stariu))
    for _ in range(len(stariu)):
        noviy.append(stariu[0]*0.6)
        stariu.remove(stariu[0])
    return sum(noviy), max(noviy)


def vtoriy(m):
    global k
    stariu = m.copy()
    novyi = []
    for _ in range(int(k*0.5)):
        novyi.append((min(stariu)*0.6))
        stariu.remove(min(stariu))
    for _ in range(len(stariu)):
        novyi.append((stariu[0]*0.65))
        stariu.remove(stariu[0])
    return  sum(novyi), max(novyi)

s1,m1 = perv(tov)
s2,m2 = vtoriy(tov)
print(max(s1,s2)-min(s1,s2),m1)