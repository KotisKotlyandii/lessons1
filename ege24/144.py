import  sys

sys.stdin = open('24data/24-j6.txt')

t = input()

nom =  1
strok = ''
for i in range(len(t)-1):
    if t[i] < t[i+1]:
        nom += 1
    else:
        strok += str(nom)
        nom = 1
# strok += str(nom)
print(strok.count('5'))
print(strok)