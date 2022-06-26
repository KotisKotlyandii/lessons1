import  sys

sys.stdin = open('24data/24-s2.txt')

t = input()
byk = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
doctor = {t.count("X%s" %i) : i for i in byk}
spisok = []
for i in doctor:
    spisok.append(i)

print(max(spisok), doctor[max(spisok)])