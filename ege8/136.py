k = 0
for s1 in 'ГЕРОЙ':
    for s2 in 'ГЕРОЙ':
        for s3 in 'ГЕРОЙ':
            for s4 in 'ГЕРОЙ':
                if s1 != 'Й' and (s1+s2+s3+s4).count('Е') + (s1+s2+s3+s4).count('О') > 0:
                    k += 1
print(k)