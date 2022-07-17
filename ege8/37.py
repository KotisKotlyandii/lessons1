k = 0
n,kon = 0,0
for s1 in 'АОУ':
    for s2 in 'АОУ':
        for s3 in 'АОУ':
            for s4 in 'АОУ':
                for s5 in 'АОУ':
                    k += 1
                    if s1+s2+s3+s4+s5 == 'УАУАУ':
                        n = k
                    elif s1+s2+s3+s4+s5 == 'ОУОУА':
                        kon = k
print(n,kon)