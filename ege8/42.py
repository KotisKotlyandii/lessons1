k = 0
for s1 in 'ЛЕТО':
    for s2 in 'ЛЕТО':
        for s3 in 'ЛЕТО':
            for s4 in 'ЛЕТО':
                if (s1+s2+s3+s4).count('Е') != 0:
                    k += 1

print(k)