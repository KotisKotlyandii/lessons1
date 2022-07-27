import  sys

sys.stdin = open('26data/26-J1.txt')

n = int(input())

a = [0] * 100
for _ in range(n):
    a[int(input())] += 1
    
k = 0
for i in range(1,50):
    k += min(a[i], a[100-i])

k += a[50] // 2
print(k)