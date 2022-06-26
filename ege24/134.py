import  sys


sys.stdin = open('24data/24-j3.txt')

t = input()

t = t.replace("TIK",'a')
t = t.replace("TOK",'a')
t = t.replace("T", ' ')
t = t.replace("I", ' ')
t = t.replace("K", ' ')
t = t.replace("O", ' ')

print(t.count('a'))