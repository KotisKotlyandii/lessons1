import sys

sys.stdin = open('24data/24-5.txt')


t = input()
kol = 0
for i in range(len(t)-2):
    if t[i:i+2] == '()':
        kol += 2
    if kol == 10000:
        print(i)