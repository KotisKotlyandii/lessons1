k = 0
for s1 in 'ПАЙЩИК':
    for s2 in 'ПАЙЩИК':
        for s3 in 'ПАЙЩИК':
            for s4 in 'ПАЙЩИК':
                for s5 in 'ПАЙЩИК':
                    for s6 in 'ПАЙЩИК':
                        if s1 != 'Й' and ('АЙ' not in s1+s2+s3+s4+s5+s6) and len(set(s1+s2+s3+s4+s5+s6)) == 6:
                            k += 1
print(k)