# import  sys
#
# sys.stdin = open('26data/26-j9.txt')

S,N = map(int,input().split())

m = []

for _ in range(N):
    m.append(int(input()))
l = []
pos = 0
while True:
    if min(m) + sum(l) > S and max(m) + sum(l) > S:
        break
    if max(m) + sum(l) <= S:
        l.append(max(m))
        pos = max(m)
        m.remove(max(m))
    else:
        m.remove(max(m))
    if min(m) + sum(l) <= S:
        l.append(min(m))
        pos = min(m)
        m.remove(min(m))
    else:
        m.remove(min(m))

print(len(l),pos)


