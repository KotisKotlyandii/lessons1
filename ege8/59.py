k = 0
for s1 in 'ПИРОГ':
    for s2 in 'ПИРОГ':
        for s3 in 'ПИРОГ':
            for s4 in 'ПИРОГ':
                for s5 in 'ПИРОГ':
                    a = s1+s2+s3+s4
                    if 0 < a.count('Р') <= 2:
                        if a.count('РО') + a.count('РИ') == a.count('Р'):
                            k += 1
                    else:
                        k += 1
print(k)