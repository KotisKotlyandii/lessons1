import  sys

sys.stdin = open('24data/24-s1.txt')

kol = 0
s = []
for _ in range(1000):
    s.append(input())

for i in s:
    for b in range(1,len(i)-2):
        if i[b-1] == "Z" and i[b+1] == "R" and i[b+2] == "O":
            kol += 1
            break

print(kol)