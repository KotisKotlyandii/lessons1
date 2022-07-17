k = 0
sed = set()
for s1 in 'ЕНИСЕЙ':
    for s2 in 'ЕНИСЕЙ':
        for s3 in 'ЕНИСЕЙ':
            for s4 in 'ЕНИСЕЙ':
                if s1 != 'Й' and (s1+s2+s3+s4).count('Е') + (s1+s2+s3+s4).count('И') > 0:
                    k += 1
                    sed.add(s1+s2+s3+s4)
print(k,len(sed))