import  sys

sys.stdin = open('24data/k8-100.txt')

tekst = input()


raaz = 1
max_k = 1
buk = ""
for i in range(len(tekst)-1):
    if tekst[i] == tekst[i+1]:
        raaz += 1
        if raaz > max_k:
            max_k = raaz
            buk = tekst[i]
    else:
        raaz = 1
print(buk, max_k)