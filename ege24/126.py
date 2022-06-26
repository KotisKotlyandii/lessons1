import sys

sys.stdin = open('24data/24-5.txt')


t = input()

t = t.replace('()','l')
t = t.replace('(', ' ')
t = t.replace(')', ' ')
spis = (list(map(str,t.split())))
print(max(spis))