k = 0
sed = set()
for s1 in 'ЩОГБА':
    for s2 in 'ЩОГБА':
        for s3 in 'ЩОГБА':
            for s4 in 'ЩОГБА':
                for s5 in 'ЩОГБА':
                    for s6 in 'ЩОГБА':
                        k += 1
                        print(k,s1+s2+s3+s4+s5+s6)
                        if s1+s2+s3+s4+s5+s6 == 'ОБЩАГА':
                            print(k)


