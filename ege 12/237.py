a = ">" + '1' * 17 + '2' * 30 + '3' * 28 + "<"
while '>1' in a or '>2' in a or '>3' in a:
    if '>1' in a:
        a = a.replace('>1', '22>',1)
    if '>2' in a:
        a = a.replace('>2', '2>1', 1)
    if '>3' in a:
        a = a.replace('>3', '1>',1)

print(a.count('1') + a.count('2') * 2 + a.count('3') * 3)