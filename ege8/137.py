k = 0
for s1 in 'ГАФНИЙ':
    for s2 in 'ГАФНИЙ':
        for s3 in 'ГАФНИЙ':
            for s4 in 'ГАФНИЙ':
                if s1 != 'Й' and (s1+s2+s3+s4).count('А') + (s1+s2+s3+s4).count('И') > 0:
                    k += 1
print(k)