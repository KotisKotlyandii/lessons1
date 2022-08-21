import  sys
sys.stdin = open('26data/26-k6.txt')

n, k = map(int,input().split())
m = []
for i in range(n):
    a,b = map(int,input().split())
    m.append((a,b,b/a))
print(m)
m.sort(key=lambda x: (x[2],-x[0]))
print(m)
x = m[:k]
s = 0
for i in x:
    s += i[0]
print(s, max(m, key=lambda x: x[0]))