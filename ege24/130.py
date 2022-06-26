import sys

sys.stdin = open('24data/24-5.txt')


t = input()
kol = 0
for i in range(len(t)):
    if t[i] == ")":
        kol += 1
    if kol == 10000:
        print(i)
        break