k = 0
for s1 in 'ВЕКНО':
    for s2 in 'ВЕКНО':
        for s3 in 'ВЕКНО':
            for s4 in 'ВЕКНО':
                for s5 in 'ВЕКНО':
                    k += 1
                    a = s1+s2+s3+s4+s5
                    if a.count('Н') == 1 and a.count('К') == 1:
                        print(k)