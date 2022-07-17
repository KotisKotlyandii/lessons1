sed = set()
k = 0

for s1 in 'АИОУЭ':
    for s2 in 'АИОУЭ':
        for s3 in 'АИОУЭ':
            for s4 in 'АИОУЭ':
                for s5 in 'АИОУЭ':
                    for s6 in 'АИОУЭ':
                        k += 1
                        if s1 == 'О' and s6 == 'О':
                            print(k,s1+s2+s3+s4+s5+s6)