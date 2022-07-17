k = 0
for s1 in 'ABCD':
    for s2 in 'ABCD':
        for s3 in 'ABCD':
           if ('AD' in (s1+s2+s3) or 'DA' not in (s1+s2+s3)) and ('BC' not in (s1+s2+s3) and 'CB' not in (s1+s2+s3)):
               k += 1

print(k)