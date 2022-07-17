k = 0
for s1 in 'АРСЕНИЙ':
    for s2 in 'АРСЕНИЙ':
        for s3 in 'АРСЕНИЙ':
            for s4 in 'АРСЕНИЙ':
                if s1 != 'Й' and (s1+s2+s3+s4).count('Е') + (s1+s2+s3+s4).count('И') + (s1+s2+s3+s4).count('А') > 0:
                    k += 1
print(k)