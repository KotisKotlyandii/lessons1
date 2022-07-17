k = 0
for s1 in 'ВНСТ':
    for s2 in 'ИНСТАВК':
        for s3 in 'ИНСТАВК':
            for s4 in 'АИ':
                k += 1
                if s1+s2+s3+s4 == 'НИКА':
                    print(k)