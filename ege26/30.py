import  sys


sys.stdin = open('26data/26-s1.txt')

kol = int(input())

b = []
m = []
for _ in range(kol):
    a = int(input())
    if a > 100:
        b.append(a)
    else:
        m.append(a)
n = []
s = 0
bol = 0
while bool(b) == True:
    n.append(max(b))
    b.remove(max(b))
    if bool(b) == True:
        bol = min(b)
        s += min(b) * 0.9
        b.remove(min(b))
if s == int(s):
    print(s+sum(n)+sum(m),bol)
else:
    print(int(s)+sum(n)+sum(m)+1,bol)