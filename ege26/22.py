import  sys

sys.stdin = open('26data/26-k2.txt')

n,k = map(int,input().split())
a = [int(input()) for _ in range(n)]
s = 0
for _ in range(k):
    a.remove(max(a))
    a.remove(min(a))

print(max(a),sum(a) // len(a))