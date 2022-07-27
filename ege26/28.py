import sys

sys.stdin = open('26data/26-J3.txt')

s,n = map(int,input().split())

a = [int(input()) for _ in range(n)]
a.sort(reverse=True)
b = []
c = []
v = 0
for i in range(n):
    if v + a[i] <= s:
        b.append(a[i])
        v += a[i]
    else:
        c.append(a[i])

print(len(b),min(b))