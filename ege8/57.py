k = 0
for s1 in 'ПИРОГ':
    for s2 in 'ПИРОГ':
        for s3 in 'ПИРОГ':
            for s4 in 'ПИРОГ':
                for s5 in 'ПИРОГ':
                        a = s1+s2+s3+s4+s5
                        if a.count('Р') == 1 and ('РИ' in a or 'РО' in a ):
                            k += 1
print(k)