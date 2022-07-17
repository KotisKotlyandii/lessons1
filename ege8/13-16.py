k = 0
for s1 in 'АКРУ':
    for s2 in 'АКРУ':
        for s3 in 'АКРУ':
            for s4 in 'АКРУ':
                for s5 in 'АКРУ':
                    k += 1
                    if s1+s2+s3+s4+s5 == 'УКАРА':
                        print(k)
