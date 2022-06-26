import  sys

sys.stdin = open('24data/24-j8.txt')

t = input()
listok = []
nom =  1
for i in range(len(t)-1):
    if int(t[i]) + int(t[i+1]) >= 10:
        nom +=  1
    else:
        listok.append(nom)
        nom = 1
listok.append(nom)
print(max(listok))
