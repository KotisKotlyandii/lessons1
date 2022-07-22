import  sys

sys.stdin = open('26data/26-k4.txt')

n,k = map(int,input().split())
a = [int(input()) for _ in range(n)]
otlich = []
xoroch = []

for _ in range(k):
    otlich.append((max(a)))
    a.remove(max(a))

for _ in range(k):
    xoroch.append((max(a)))
    a.remove(max(a))

print(sum(xoroch) // k, sum(otlich) // k)