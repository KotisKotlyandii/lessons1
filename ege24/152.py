import  sys

sys.stdin = open('24data/24-j9.txt')

t = input()
kol = 0
for i in range(len(t) // 2):
    if t[i] == t[len(t) - len(t[0:i + 1])]:
        kol += 1

print(kol)