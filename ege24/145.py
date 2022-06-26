import  sys

sys.stdin = open('24data/24-j7.txt')

t = input()
listok = []
nom =  1
for i in range(len(t)-1):
    if int(t[i]) % 2 ==  int(t[i+1]) % 2:
        nom +=  1
    else:
        listok.append(nom)
        nom = 1
listok.append(nom)
print(max(listok))
