a = '5' * 13 + '53' * 16 + '4' * 23 + '3'
while '43' in a or '53' in a:
    if '43' in a:
        a = a.replace('43','33',1)
    else:
        a = a.replace('53','433',1)
print(a.count('3'))