k = 0
for s1 in 'КРАН':
    for s2 in 'КРАН':
        for s3 in 'КРАН':
            if (s1+s2+s3).count('А') != 0:
                k += 1

print(k)