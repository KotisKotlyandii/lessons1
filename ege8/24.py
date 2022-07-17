k = 0
for s1 in 'МАРТ':
    for s2 in 'МАРТ':
        for s3 in 'МАРТ':
            for s4 in 'МАРТ':
                for s5 in 'МАРТ':
                    for s6 in 'МАРТ':
                        if (s1+s2+s3+s4+s5+s6).count('Р') == 2:
                            k += 1

print(k)
