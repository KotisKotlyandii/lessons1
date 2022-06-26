import  sys


sys.stdin = open('24data/24-157.txt')

t = input()
byk = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
doctor = {i:0 for i in byk}

for i in range(len(t)-2):
    if len(set(t[i:i+2])) == 1:
        doctor[t[i+2]] += 1

vtor = {doctor[i] : i for i in doctor}
spisok = []
for i in vtor:
    spisok.append(i)
