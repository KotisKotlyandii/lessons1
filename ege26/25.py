import  sys

sys.stdin = open('26data/26-k5.txt')

n,k,m = map(int,input().split())
a = [int(input()) for _ in range(n)]
premium = []
byd = []

for _ in range(k):
    byd.append(min(a))
    a.remove(min(a))

for _ in range(m):
    premium.append(max(a))
    a.remove(max(a))

print(min(premium),sum(byd) // k)
