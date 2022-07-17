k = 0
for s1 in 'АГИЛМОРТ':
    for s2 in 'АГИЛМОРТ':
        for s3 in 'АГИЛМОРТ':
            for s4 in 'АГИЛМОРТ':
                k += 1
                if s3+s4 == 'ИМ':
                    print(k)