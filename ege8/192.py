k = 0
spis = list()
for s1 in 'МАРИ':
    for s2 in 'МАРИ':
        for s3 in 'МАРИ':
            for s4 in 'МАРИ':
                for s5 in 'ИНА':
                    for s6 in 'ИНА':
                        for s7 in 'ИНА':
                            for s8 in 'ИНА':
                                if len(set(s1+s2+s3+s4)) == 4:
                                    spis.append(s1+s2+s3+s4+s5+s6+s7+s8)

spis.sort()
for i in range(len(spis)):
    if spis[i] == 'МАРИАННА':
        print(i+1)

