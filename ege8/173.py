sed = set()
k = 0
for s1 in 'ЕЛЕЙ':
    for s2 in 'ЕЛЕЙ':
        for s3 in 'ЕЛЕЙ':
            for s4 in 'ЕЛЕЙ':
                for s5 in 'ЕЛЕЙ':
                    for s6 in 'ЕЛЕЙ':
                        a = s1+s2+s3+s4+s5
                        if a.count('Й') <= 1 and s1 != 'Й' and s5 != 'Й' and ('ЙЕ' not in a) and ('ЕЙ' not in a):
                            sed.add(a)
                            k += 1
print(len(sed),k)