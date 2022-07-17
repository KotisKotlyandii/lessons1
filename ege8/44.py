k = 0
for s1 in 'КЛОУН':
    for s2 in 'КЛОУН':
        for s3 in 'КЛОУН':
            for s4 in 'КЛОУН':
                if (s1+s2+s3+s4).count('У') != 0:
                    k += 1

print(k)