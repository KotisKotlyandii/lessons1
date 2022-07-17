k = 0
for s1 in 'СЛОН':
    for s2 in 'СЛОН':
        for s3 in 'СЛОН':
            for s4 in 'СЛОН':
                for s5 in 'СЛОН':
                    if 0 < (s1+s2+s3+s4+s5).count('О') <= 3:
                        k += 1
print(k)