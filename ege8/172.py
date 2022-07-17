sed = set()
k = 0
for s1 in 'СОЛОВЕЙ':
    for s2 in 'СОЛОВЕЙ':
        for s3 in 'СОЛОВЕЙ':
            for s4 in 'СОЛОВЕЙ':
                for s5 in 'СОЛОВЕЙ':
                    for s6 in 'СОЛОВЕЙ':
                        a = s1+s2+s3+s4+s5+s6
                        if a.count('Й') <= 1 and s1 != 'Й' and s6 != 'Й' and ('ЙЕ' not in a) and ('ЕЙ' not in a):
                            sed.add(a)
print(len(sed))