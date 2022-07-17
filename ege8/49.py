k = 0
for s1 in 'КАТЕР':
    for s2 in 'КАТЕР':
        for s3 in 'КАТЕР':
            if (s1+s2+s3).count('Р') >= 2:
                k += 1

print(k)