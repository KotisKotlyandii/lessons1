import  sys

sys.stdin = open('24data/24-s1.txt')

kol = 0
s = []
for _ in range(1000):
    s.append(input())

for i in s:
    for b in range(1,len(i)-1):
        if i[b-1] == "A" and i[b+1] == "R":
            kol += 1
            break

print(kol)