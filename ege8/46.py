k = 0
for s1 in 'БАЛКОН':
    for s2 in 'БАЛКОН':
        for s3 in 'БАЛКОН':
            k += 1
            if (s1+s2+s3).count('Б') != 0:
                k += 1
print(k)