sed = set()
k = 0
for s1 in 'МОЛОКО':
    for s2 in 'МОЛОКО':
        for s3 in 'МОЛОКО':
            for s4 in 'МОЛОКО':
                for s5 in 'МОЛОКО':
                    for s6 in 'МОЛОКО':
                        a = s1+s2+s3+s4+s5+s6
                        if len(set(a)) == 4 and a.count('О') == 3:
                            k += 1
                            sed.add(s1+s2+s3+s4+s5+s6)
print(len(sed),k)