sed = set()
k = 0
for s1 in 'КАЛИЙ':
    for s2 in 'КАЛИЙ':
        for s3 in 'КАЛИЙ':
            for s4 in 'КАЛИЙ':
                for s5 in 'КАЛИЙ':
                    for s6 in 'КАЛИЙ':
                        a = s1+s2+s3+s4+s5
                        if a.count('Й') <= 1 and s1 != 'Й' and s5 != 'Й' and ('ИЕ' not in a) and ('ЕИ' not in a):
                            sed.add(a)
                            k += 1
print(len(sed),k)