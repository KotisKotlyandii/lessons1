a = '1'*31 + '2' * 24 + '3' * 46 + '0'
while '30' in a or '3103' in a or '1201' in a:
    a = a.replace('30','01',1)
    a = a.replace('3103','02',1)
    a = a.replace('1201','03',1)
print(a.count('3'))