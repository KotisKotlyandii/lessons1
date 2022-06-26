import  sys


sys.stdin = open('24data/24-153.txt')

t = input()

t = t.replace('A', ' ')
t = t.replace('B', ' ')
t = t.replace('C', ' ')
t = t.replace('E', ' ')
t = t.replace('F', ' ')

print(len(max(list(map(str,t.split())))))
print(list(map(str,t.split())))
print(max(list(map(str,t.split()))))