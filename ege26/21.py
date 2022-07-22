import  sys

sys.stdin = open('26data/26-k1.txt')

n,k = map(int,input().split())
a = [int(input()) for _ in range(n)]
s = 0
for _ in range(k):
    s += max(a) * 0.2
    a.remove(max(a))

print(max(a),int(s))