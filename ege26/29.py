import  sys

sys.stdin = open('26data/26-j4.txt')
n = int(input())
sp = [int(input()) for _ in range(n)]

yd = int(n*0.1)

for _ in range(yd):
    sp.remove(max(sp))

for _ in range(yd):
    sp.remove(min(sp))

print(sum(sp), max(sp))