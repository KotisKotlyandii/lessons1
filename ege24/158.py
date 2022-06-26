import  sys


sys.stdin = open('24data/24-157.txt')

t = input()
byk = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
doctor = {i:0 for i in byk}

for i in range(len(t)-2):
    if len(set(t[i+1:i+3])) == 1:
        doctor[t[i]] += 1

vtor = {doctor[i] : i for i in doctor}
spisok = []
for i in vtor:
    spisok.append(i)

print(max(spisok), vtor[max(spisok)])