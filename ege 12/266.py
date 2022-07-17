a = '1'*30 + '2' * 39 + '3' * 42 + '0'
while '302' in a or '3103' in a or '20' in a:
    a = a.replace('302','01',1)
    a = a.replace('3103','02',1)
    a = a.replace('20','03',1)
print(a.count('2'))