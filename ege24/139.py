import  sys

sys.stdin = open('24data/24-s1.txt')

kol = 0
s = []
for _ in range(1000):
    s.append(input())

for i in s:
    if i.count('S') == i.count('X'):
        kol += 1

print(kol)