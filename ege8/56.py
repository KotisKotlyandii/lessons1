k = 0
for s1 in 'СИРОП':
    for s2 in 'СИРОП':
        for s3 in 'СИРОП':
            for s4 in 'СИРОП':
                for s5 in 'СИРОП':
                        a = s1+s2+s3+s4+s5
                        if a.count('О') == 1 and ('ПО' in a or 'РО' in a or 'СО' in a ):
                            k += 1
print(k)