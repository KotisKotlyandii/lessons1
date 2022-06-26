import sys


sys.stdin = open('24data/24-j1.txt')

t = input()

t = t.replace("КОТ", 'a')
t = t.replace('К',' ')
t = t.replace('О',' ')
t = t.replace('Т',' ')
print(len(max(list(map(str,t.split())))))