k = 0
sed = set()
for s1 in 'АКЛОШ':
    for s2 in 'АЛКОШ':
        for s3 in 'АЛКОШ':
            for s4 in 'АЛКОШ':
                for s5 in 'АЛКОШ':
                    a = s1+s2+s3+s4+s5
                    if a.count('А') + a.count('О') >= 1:
                        k += 1
                        sed.add(a)
print(len(sed),k)

