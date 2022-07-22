import sys

sys.stdin = open('26data/26-9.txt')

s,n = map(int,input().split())
a = [int(input()) for _ in range(n)]
a.sort()
print(s, n)
b = []
for i in range(n):
    if sum(b) + a[i] <= s:
        b.append(a[i])
        a[i] = 0
print(len(b))
ost = s - sum(b[:-1])
c = [i for i in a if i <= ost]
print(max(c))