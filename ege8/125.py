sed = set()
k = 0
for s1 in 'ТРАТАТА':
    for s2 in 'ТРАТАТА':
        for s3 in 'ТРАТАТА':
            for s4 in 'ТРАТАТА':
                for s5 in 'ТРАТАТА':
                    for s6 in 'ТРАТАТА':
                        for s7 in 'ТРАТАТА':
                            k += 1
                            sed.add(s1+s2+s3+s4+s5+s6+s7)
print(len(sed),k)