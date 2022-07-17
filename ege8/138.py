k = 0
for s1 in 'МОИСЕЙ':
    for s2 in 'МОИСЕЙ':
        for s3 in 'МОИСЕЙ':
            for s4 in 'МОИСЕЙ':
                if s1 != 'Й' and (s1+s2+s3+s4).count('О') + (s1+s2+s3+s4).count('И') + (s1+s2+s3+s4).count('Е') > 0:
                    k += 1
print(k)