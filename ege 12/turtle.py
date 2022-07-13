a = '1' * 50 + '2' * 50 + '3' * 50
while '12' in a or '32' in a or '31' in a:
    if '12' in a:
        a = a.replace('12','21',1)
    if '32' in a:
        a = a.replace('32','23',1)
    if '31' in a:
        a = a.replace('31','13',1)

print(a[19] + a[79] + a[119])