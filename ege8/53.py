k = 0
for s1 in 'МУХА':
    for s2 in 'МУХА':
        for s3 in 'МУХА':
            for s4 in 'МУХА':
                for s5 in 'МУХА':
                    if (s1+s2+s3+s4+s5).count('У') <= 3:
                        k += 1
print(k)