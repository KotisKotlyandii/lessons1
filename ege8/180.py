sed = set()
k = 0
for s1 in 'МЕЧТА':
    for s2 in 'МЕЧТА':
        for s3 in 'МЕЧТА':
            for s4 in 'МЕЧТА':
                for s5 in 'МЕЧТА':
                    for s6 in 'МЕЧТА':
                        if (s1+s2+s3+s4+s5+s6).count('А') >= 3:
                            sed.add(s1+s2+s3+s4+s5+s6)
                            k += 1
print(len(sed),k)