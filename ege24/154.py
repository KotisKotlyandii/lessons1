import  sys

sys.stdin = open('24data/24-153.txt')

t = input()

t = t.replace('A', ' ')
t = t.replace('B', ' ')
t = t.replace('C', ' ')
t = t.replace('E', ' ')
t = t.replace('F', ' ')

listok = list(map(str,t.split()))
vtor = [i for i in listok if len(i) % 2 == 0 and len(i) != 2 ]
print(len(min(vtor)))