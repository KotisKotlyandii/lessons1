import  sys


sys.stdin = open('24data/24-169.txt')

t = input()

t = t.replace('XYZ','A')
t = t.replace('X', ' ')
t = t.replace('Y', ' ')
t = t.replace('Z', ' ')

print(len(max(list(map(str,t.split())))))