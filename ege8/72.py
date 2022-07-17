k = 0
for s1 in 'АКЛОШ':
    for s2 in 'АЛКОШ':
        for s3 in 'АЛКОШ':
            for s4 in 'АЛКОШ':
                k += 1
                print(k,s1+s2+s3+s4)
                if s1 == 'О':
                    print(k)