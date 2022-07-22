kol = int(input())
a = input()
k = 0
while 'xxx' in a:
    a = a.replace('xxx','xx',1)
    k += 1

print(k)