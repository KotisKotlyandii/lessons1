import sys

sys.stdin = open('24data/24-1.txt')

tekst = input()
tekts2 = ''
for i in tekst:
    if i in "13579":
        tekts2 += i
    else:
        tekts2 += ' '
print(max(map(int,tekts2.split())))