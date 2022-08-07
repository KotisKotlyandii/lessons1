import sys

sys.stdin = open('26data/26-j6.txt')

n = int(input())

a = [int(input()) for _ in range(n)]

ob = sum(a) * 0.9
print(ob)
a.sort(reverse= True)

b = a.copy()
k = 0
for i in range(1,n):
    if sum(b[:i])*0.8 + sum(b[i:]) <= ob:
        k = i
        break
print(n - k)
d = ob - sum(b[:k+1])*0.8 - sum(b[k+1:])
print(d)
for i in range(0, k+1):
    if a[i]*0.2 < d:
        print(a[i])
        break