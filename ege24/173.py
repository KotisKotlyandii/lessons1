import  sys


sys.stdin = open('24data/24-173.txt')

t = input()

setik = set()
prosh = 0
spisok = []
kol = 0
for i in range(len(t)-2):
    setik.add(t[i:i+3])
    if setik == prosh:
        spisok.append(kol)
    else:
        kol += 1
        prosh = setik.copy()
print(max(spisok))