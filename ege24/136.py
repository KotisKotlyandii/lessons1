import  sys


sys.stdin = open('24data/24-j5.txt')

t = input()

t = t.replace('STOCK', "S")
t = t.replace("OCK", "A")
print(t.count('A'))