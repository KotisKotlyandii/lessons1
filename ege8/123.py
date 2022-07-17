sed = set()
k = 0
for s1 in 'АССАСИН':
    for s2 in 'АССАСИН':
        for s3 in 'АССАСИН':
            for s4 in 'АССАСИН':
                for s5 in 'АССАСИН':
                    for s6 in 'АССАСИН':
                        for s7 in 'АССАСИН':
                            k += 1
                            sed.add(s1+s2+s3+s4+s5+s6+s7)
print(len(sed),k)