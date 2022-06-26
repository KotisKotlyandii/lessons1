import  sys


sys.stdin = open('24data/24-153.txt')

t = input()

nachalo = 0
kol = 0
listok = []
for i in range(len(t)):
    if t[i] == "A" and nachalo != 1:
        nachalo = 1
        kol += 1
    elif nachalo == 1 and t[i] != "F":
        kol += 1
    else:
        kol += 1
        listok.append(kol)
        kol = 0
        nachalo = 0
vtor = [i for i in listok if i > 2 and 7 <= i <= 10]
print(len(vtor))