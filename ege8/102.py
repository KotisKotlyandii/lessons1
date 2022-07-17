k = 0
for s1 in 'НИГРОЛ':
    for s2 in 'НИГРОЛ':
        for s3 in 'НИГРОЛ':
            for s4 in 'НИГРОЛ':
                for s5 in 'НИГРОЛ':
                    for s6 in 'НИГРОЛ':
                        if len(set(s1+s2+s3+s4+s5+s6)) == 6 and s1 != 'О' and ("ОИГ" not in s1+s2+s3+s4+s5+s6):
                            k += 1
print(k)