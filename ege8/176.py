sed = set()
k = 0
for s1 in 'СЧИТАЙ':
    for s2 in 'СЧИТАЙ':
        for s3 in 'СЧИТАЙ':
            for s4 in 'СЧИТАЙ':
                if (s1+s2+s3+s4).count('А') <= 1:
                    sed.add(s1+s2+s3+s4)
                    k += 1
print(len(sed),k)