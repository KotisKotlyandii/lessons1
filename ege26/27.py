import  sys

sys.stdin = open('26data/26-J2.txt')

n = int(input())
print(n)
a = [0] * 10001

for i in range(n):
    a[int(input())] += 1
s = 0
for i in range(10001):
    s  += i * a[i]
sr = s / n
k = 0
el = 0
for i in range(10001):
    k += a[i]
    if k > n//2:
      el = i
      break

print(sr,el)
c = a[5004:5008]
print(sum(c))
