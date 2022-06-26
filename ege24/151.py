import  sys


sys.stdin = open('24data/24-j9.txt')

t = input()

kol = 0
for i in range(len(t)-5):
    tek = t[i:i+5]
    if tek == tek[::-1]:
       kol += 1

print(kol)
