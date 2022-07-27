import sys

sys.stdin = open('26data/26-k3.txt')

n,k,m = map(int,input().split())

a = [int(input()) for _ in range(n)]

a.sort(reverse=True)
print(a)
pob = a[:k]
priz = a[k:m+k]
print(min(priz),min(pob))