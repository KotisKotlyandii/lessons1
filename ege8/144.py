k = 0
sed = set()
for s1 in 'АЗИМУТ':
    for s2 in 'АЗИМУТ':
        for s3 in 'АЗИМУТ':
            for s4 in 'АЗИМУТ':
                for s5 in 'АЗИМУТ':
                    for s6 in 'АЗИМУТ':
                        a = s1+s2+s3+s4+s5+s6
                        if a.count('З') + a.count('М') + a.count('Т') >= 3:
                            k += 1
                            sed.add(a)
print(k,len(sed))