a = '1'*58 + '2' * 23 + '3' * 15 + '0'
while '2302' in a or '10' in a or '201' in a:
    a = a.replace('2302','01',1)
    a = a.replace('10','02',1)
    a = a.replace('201','03',1)
print(a.count('2'))